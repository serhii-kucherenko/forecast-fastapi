import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from services import reports_service

templates = Jinja2Templates(directory="templates")
router = fastapi.APIRouter()


@router.get('/')
async def index(request: Request):
    reports = await reports_service.get_reports()
    data = {'request': request, 'reports': reports}

    return templates.TemplateResponse('/home/index.html', data)


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
