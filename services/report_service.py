from typing import List

from models.location import Location
from models.report import Report

__reports: List[Report] = []


async def get_reports() -> List[Report]:

    # Would be an async call here.
    return list(__reports)


async def add_report(description:str, locations: Location) -> Report:
    report = Report(description=description, location=locations)

    # Simulate saving to DB.
    # Would be an async call here.
    __reports.append(report)
    __reports.sort(key=lambda item: item.created_date, reverse=True)

    return report;