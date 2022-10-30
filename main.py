import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather
from views import home

app = fastapi.FastAPI(
    # Uncomment for production mode
    # docs_url=None
)


def configure():
    configure_routing()


def configure_routing():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(weather.router)


# In development
if __name__ == '__main__':
    configure()
    uvicorn.run(app, port=8000, host='127.0.0.1')
# In production
else:
    configure()
