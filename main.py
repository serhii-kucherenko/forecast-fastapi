import asyncio
import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles


from api import weather
from models.location import Location
from services import open_weather_service, reports_service
from views import home

api = fastapi.FastAPI(
    # Uncomment for production mode
    # docs_url=None
)


def configure():
    configure_routing()
    configure_weather_api_keys()
    configure_fake_data()


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather.router)


def configure_weather_api_keys():
    file_path = 'settings.json'
    file = Path(file_path).absolute()

    if not file.exists():
        print(f"Warning: {file} does not exist")
        raise Exception(f"Error: {file} does not exist")

    with open(file_path) as settingsFile:
        settings = json.load(settingsFile)
        open_weather_service.api_key = settings['api_key']


def configure_fake_data():
    # This was added to make it easier to test the weather event reporting
    # We have /api/reports but until you submit new data each run, it's missing
    # So this will give us something to start from.

    # Changed this from the video due to changes in Python 3.10:
    # DeprecationWarning: There is no current event loop, loop = asyncio.get_event_loop()
    loop = asyncio.new_event_loop()

    try:
        loc = Location(city="Lviv", country="UA")
        loop.run_until_complete(reports_service.add_report("Misty sunrise today, beautiful!", loc))
        loop.run_until_complete(reports_service.add_report("Clouds over downtown.", loc))
    except RuntimeError:
        print("Fake starter data will no appear on home page.")
        print("Once you add data with the client, it will appear properly.")


# In development
if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
# In production
else:
    configure()