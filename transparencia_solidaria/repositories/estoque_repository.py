from sqlalchemy import select, case
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from transparencia_solidaria.models.estoque_model import Entidade, ItemEstoque


async def buscar_itens(
    db: AsyncSession,
    categoria: str | None = None,
    entidade_id: int | None = None,
    skip: int = 0,
    limit: int = 20,
):
    stmt = (
        select(ItemEstoque)
        .options(selectinload(ItemEstoque.entidade))
        .order_by(ItemEstoque.id.desc())
    )

    if categoria:
        stmt = stmt.where(ItemEstoque.categoria == categoria)

    if entidade_id:
        stmt = stmt.where(ItemEstoque.entidade_id == entidade_id)

    stmt = stmt.offset(skip).limit(limit)

    result = await db.execute(stmt)
    return result.scalars().all()


async def listar_categorias(db: AsyncSession):
    stmt = (
        select(ItemEstoque.categoria).distinct().order_by(ItemEstoque.categoria.asc())
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def listar_entidades(db: AsyncSession, categoria: str | None = None):
    stmt = select(Entidade).join(ItemEstoque, ItemEstoque.entidade_id == Entidade.id)

    if categoria:
        stmt = stmt.where(ItemEstoque.categoria == categoria)

    stmt = stmt.distinct().order_by(Entidade.nome.asc())

    result = await db.execute(stmt)
    return result.scalars().all()


async def buscar_entidade_por_id(db: AsyncSession, entidade_id: int):
    stmt = select(Entidade).where(Entidade.id == entidade_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def buscar_itens(
    db: AsyncSession,
    categoria: str | None = None,
    entidade_id: int | None = None,
    ordenar_por: str = 'id',
    ordem: str = 'desc',
    skip: int = 0,
    limit: int = 20,
):
    status_ordenacao = case(
        (ItemEstoque.quantidade_atual <= 0, 0),
        (ItemEstoque.quantidade_atual < ItemEstoque.quantidade_necessaria, 1),
        else_=2,
    )

    colunas_ordenacao = {
        'id': ItemEstoque.id,
        'produto': ItemEstoque.produto,
        'categoria': ItemEstoque.categoria,
        'quantidade_atual': ItemEstoque.quantidade_atual,
        'quantidade_necessaria': ItemEstoque.quantidade_necessaria,
        'unidade': ItemEstoque.unidade,
        'atualizado_em': ItemEstoque.atualizado_em,
        'entidade': Entidade.nome,
        'status': status_ordenacao,
    }

    coluna = colunas_ordenacao.get(ordenar_por, ItemEstoque.id)

    stmt = (
        select(ItemEstoque)
        .join(Entidade, ItemEstoque.entidade_id == Entidade.id)
        .options(selectinload(ItemEstoque.entidade))
    )

    if categoria:
        stmt = stmt.where(ItemEstoque.categoria == categoria)

    if entidade_id:
        stmt = stmt.where(ItemEstoque.entidade_id == entidade_id)

    if ordem == 'asc':
        stmt = stmt.order_by(coluna.asc())
    else:
        stmt = stmt.order_by(coluna.desc())

    stmt = stmt.offset(skip).limit(limit)

    result = await db.execute(stmt)
    return result.scalars().all()
