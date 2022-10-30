import fastapi
from typing import Optional
from fastapi import Depends
from models.location import Location

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    return f"City: {loc.city}, State: {loc.state}, Country: {loc.country}, Units: {units}"
