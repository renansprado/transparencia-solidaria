# from typing import Annotated

# from fastapi import Depends, Query
# from fastapi.requests import Request
# from fastapi.routing import APIRouter
# from sqlalchemy.ext.asyncio import AsyncSession

# from transparencia_solidaria.core.configs import settings
# from transparencia_solidaria.core.database import get_db
# from transparencia_solidaria.repositories import estoque_repository as repo


# router = APIRouter()

# DbDep = Annotated[AsyncSession, Depends(get_db)]


# @router.get('/estoque_lista', name='estoque_lista')
# async def lista_estoque(
#     request: Request,
#     db: DbDep,
#     categoria: Annotated[str | None, Query(description='Filtrar por categoria')] = None,
#     pagina: Annotated[int, Query(ge=1, description='Número da página')] = 1,
#     por_pagina: Annotated[int, Query(ge=5, le=100, description='Itens por página')] = 20,
# ):
#     skip = (pagina - 1) * por_pagina

#     if categoria:
#         itens = await estoque_repository.buscar_itens_por_categoria(db, categoria, skip=skip, limit=por_pagina)
#     else:
#         itens = await estoque_repository.listar_itens(db, skip=skip, limit=por_pagina)

#     categorias = await estoque_repository.listar_categorias(db)

#     context = {
#         'request': request,
#         'itens': itens,
#         'categorias': categorias,
#         'categoria_selecionada': categoria,
#         'pagina': pagina,
#         'por_pagina': por_pagina,
#         'total_itens': len(itens),
#     }
#     return settings.TEMPLATES.TemplateResponse(name='estoque/lista.html', request=request, context=context)

from typing import Annotated

from fastapi import Depends, Query
from fastapi.requests import Request
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from transparencia_solidaria.core.configs import settings
from transparencia_solidaria.core.database import get_db
from transparencia_solidaria.repositories import estoque_repository

router = APIRouter()

DbDep = Annotated[AsyncSession, Depends(get_db)]


@router.get("/estoque_lista/", name="estoque_lista")
async def lista_estoque(
    request: Request,
    db: DbDep,
    categoria: Annotated[str | None, Query(description="Filtrar por categoria")] = None,
    entidade: Annotated[str | None, Query(description="Filtrar por entidade")] = None,
    ordenar_por: Annotated[str, Query(description='Coluna de ordenação')] = 'id',
    ordem: Annotated[str, Query(description='Direção da ordenação')] = 'desc',
    pagina: Annotated[int, Query(ge=1, description="Número da página")] = 1,
    por_pagina: Annotated[
        int, Query(ge=5, le=100, description="Itens por página")
    ] = 20,
):
    skip = (pagina - 1) * por_pagina
    entidade_id = int(entidade) if entidade else None

    itens = await estoque_repository.buscar_itens(
        db,
        categoria=categoria,
        entidade_id=entidade_id,
        ordenar_por=ordenar_por,
        ordem=ordem,
        skip=skip,
        limit=por_pagina,
    )

    categorias = await estoque_repository.listar_categorias(db)
    entidades = await estoque_repository.listar_entidades(db, categoria=categoria)

    entidade_nome_selecionada = None
    if entidade_id:
        entidade_obj = await estoque_repository.buscar_entidade_por_id(db, entidade_id)
        if entidade_obj:
            entidade_nome_selecionada = entidade_obj.nome

    context = {
        "request": request,
        "itens": itens,
        "categorias": categorias,
        "entidades": entidades,
        "categoria_selecionada": categoria,
        "entidade_selecionada": entidade_id,
        "entidade_nome_selecionada": entidade_nome_selecionada,
        "ordenar_por": ordenar_por,
        "ordem": ordem,
        "pagina": pagina,
        "por_pagina": por_pagina,
        "total_itens": len(itens),
    }

    return settings.TEMPLATES.TemplateResponse(
        name="estoque/lista.html",
        request=request,
        context=context,
    )
