from typing import Optional

api_key: Optional[str] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    q = f'{city},{state},{country}'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&units={units}&appid={api_key}"
    print(url)
