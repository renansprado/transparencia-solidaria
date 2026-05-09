import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from transparencia_solidaria.views import home_view, estoque_view

app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(home_view.router)
app.include_router(estoque_view.router)

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, log_level='info')
