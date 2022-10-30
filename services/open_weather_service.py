from typing import Optional

import httpx
import requests

from infrastructure import weather_cache

api_key: Optional[str] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&units={units}&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    forecast = data["main"]

    return forecast


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if forecast := weather_cache.get_weather(city, state, country, units):
        return forecast

    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&units={units}&appid={api_key}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    data = response.json()
    forecast = data["main"]

    weather_cache.set_weather(city, state, country, units, forecast)

    return forecast
