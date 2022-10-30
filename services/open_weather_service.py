from typing import Optional

import requests

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
