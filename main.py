import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles


from api import weather
from services import open_weather_service
from views import home

api = fastapi.FastAPI(
    # Uncomment for production mode
    # docs_url=None
)


def configure():
    configure_routing()
    configure_weather_api_keys()


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


# In development
if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
# In production
else:
    configure()