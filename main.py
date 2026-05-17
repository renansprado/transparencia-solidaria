import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from transparencia_solidaria.views import home_view, estoque_view, entidade_view

app = FastAPI(docs_url=None, redoc_url=None)

class HTTPSProxyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request.scope["scheme"] = "https"
        return await call_next(request)

app.add_middleware(HTTPSProxyMiddleware)

app.include_router(home_view.router)
app.include_router(estoque_view.router)
app.include_router(entidade_view.router)

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, log_level='info')
