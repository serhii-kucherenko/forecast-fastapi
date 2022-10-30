import fastapi
from typing import Optional, List
from fastapi import Depends
from models.location import Location
from models.report import Report, ReportSubmittal
from models.validation_error import ValidationError
from services import open_weather_service, reports_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await open_weather_service.get_report_async(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.message, status_code=ve.status_code)
    except Exception as ex:
        return fastapi.Response(content=str(ex), status_code=500)


@router.get('/api/reports', name='all_reports')
async def reports() -> List[Report]:
    # For testing purposes, we'll just return the reports in memory.
    # await reports_service.add_report('Test', Location(city='London', country='UK'))
    # await reports_service.add_report('Test2', Location(city='Lviv', country='UA'))
    return await reports_service.get_reports()


@router.post('/api/reports', name='add_report')
async def add_report(report: ReportSubmittal) -> Report:
    return await reports_service.add_report(description=report.description, location=report.location)