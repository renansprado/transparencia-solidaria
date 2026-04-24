from fastapi.requests import Request
from fastapi.routing import APIRouter

from transparencia_solidaria.core.configs import settings

router = APIRouter()


@router.get('/', name='index')
async def index(request: Request):
    context = {'request': request}
    return settings.TEMPLATES.TemplateResponse(name='index.html', **context)
