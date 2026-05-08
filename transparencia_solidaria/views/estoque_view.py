from typing import Annotated

from fastapi import Depends, Query
from fastapi.requests import Request
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from transparencia_solidaria.core.configs import settings
from transparencia_solidaria.core.database import get_db
from transparencia_solidaria.repositories import estoque_repository as repo

router = APIRouter(prefix='/estoque', tags=['estoque'])

DbDep = Annotated[AsyncSession, Depends(get_db)]


@router.get('/', name='estoque_lista')
async def lista_estoque(
    request: Request,
    db: DbDep,
    categoria: Annotated[str | None, Query(description='Filtrar por categoria')] = None,
    pagina: Annotated[int, Query(ge=1, description='Número da página')] = 1,
    por_pagina: Annotated[int, Query(ge=5, le=100, description='Itens por página')] = 20,
):
    skip = (pagina - 1) * por_pagina

    if categoria:
        itens = await repo.buscar_itens_por_categoria(db, categoria, skip=skip, limit=por_pagina)
    else:
        itens = await repo.listar_itens(db, skip=skip, limit=por_pagina)

    categorias = await repo.listar_categorias(db)

    context = {
        'request': request,
        'itens': itens,
        'categorias': categorias,
        'categoria_selecionada': categoria,
        'pagina': pagina,
        'por_pagina': por_pagina,
        'total_itens': len(itens),
    }
    return settings.TEMPLATES.TemplateResponse(name='estoque/lista.html', context=context)
