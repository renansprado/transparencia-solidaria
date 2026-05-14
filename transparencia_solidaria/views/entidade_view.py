from typing import Annotated

from fastapi import Depends, Query, HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from transparencia_solidaria.core.configs import settings
from transparencia_solidaria.core.database import get_db
from transparencia_solidaria.repositories import entidade_repository

router = APIRouter()

DbDep = Annotated[AsyncSession, Depends(get_db)]


@router.get("/entidades/", name="entidade_lista")
async def lista_entidades(
    request: Request,
    db: DbDep,
    estado: Annotated[
        str | None, Query(description="Filtrar por sigla do estado")
    ] = None,
    cidade: Annotated[
        str | None, Query(description="Filtrar por nome da cidade")
    ] = None,
    ordenar_por: Annotated[str, Query(description="Coluna de ordenação")] = "nome",
    ordem: Annotated[str, Query(description="Direção da ordenação")] = "asc",
    pagina: Annotated[int, Query(ge=1, description="Número da página")] = 1,
    por_pagina: Annotated[
        int, Query(ge=5, le=100, description="Itens por página")
    ] = 20,
):
    skip = (pagina - 1) * por_pagina

    entidades = await entidade_repository.listar_entidades(
        db,
        estado_sigla=estado,
        cidade_nome=cidade,
        ordenar_por=ordenar_por,
        ordem=ordem,
        skip=skip,
        limit=por_pagina,
    )

    estados = await entidade_repository.listar_estados(db)
    cidades = await entidade_repository.listar_cidades(db, estado_sigla=estado)

    context = {
        "request": request,
        "entidades": entidades,
        "estados": estados,
        "cidades": cidades,
        "estado_selecionado": estado,
        "cidade_selecionada": cidade,
        "ordenar_por": ordenar_por,
        "ordem": ordem,
        "pagina": pagina,
        "por_pagina": por_pagina,
        "total_entidades": len(entidades),
    }

    return settings.TEMPLATES.TemplateResponse(
        name="entidade_lista.html",
        request=request,
        context=context,
    )


@router.get("/entidades/{entidade_id}", name="entidade_detalhe")
async def detalhe_entidade(
    request: Request,
    entidade_id: int,
    db: DbDep,
):
    entidade = await entidade_repository.buscar_entidade_por_id(db, entidade_id)

    if not entidade:
        raise HTTPException(status_code=404, detail="Entidade não encontrada")

    context = {
        "request": request,
        "entidade": entidade,
    }

    return settings.TEMPLATES.TemplateResponse(
        name="entidade.html",  # reutiliza o template já existente no projeto
        request=request,
        context=context,
    )


@router.get("/entidades/cidades-por-estado", name="entidade_cidades_parcial")
async def cidades_por_estado(
    request: Request,
    db: DbDep,
    estado: Annotated[str | None, Query()] = None,
):
    cidades = await entidade_repository.listar_cidades(db, estado_sigla=estado)
    options_html = '<option value="">Todas</option>'
    for c in cidades:
        options_html += f'<option value="{c.nome}">{c.nome}</option>'
    return HTMLResponse(content=options_html)
