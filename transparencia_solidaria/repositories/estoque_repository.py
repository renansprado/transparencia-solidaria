from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from transparencia_solidaria.models.estoque_model import Entidade, ItemEstoque


async def listar_entidades(db: AsyncSession, skip: int = 0, limit: int = 50) -> list[Entidade]:
    """Retorna entidades com seus itens de estoque carregados."""
    stmt = (
        select(Entidade)
        .options(selectinload(Entidade.itens))
        .order_by(Entidade.nome)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def listar_itens(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[ItemEstoque]:
    """Retorna itens de estoque com a entidade relacionada."""
    stmt = (
        select(ItemEstoque)
        .options(selectinload(ItemEstoque.entidade))
        .order_by(ItemEstoque.categoria, ItemEstoque.produto)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def buscar_itens_por_categoria(
    db: AsyncSession, categoria: str, skip: int = 0, limit: int = 100
) -> list[ItemEstoque]:
    """Filtra itens por categoria."""
    stmt = (
        select(ItemEstoque)
        .options(selectinload(ItemEstoque.entidade))
        .where(ItemEstoque.categoria == categoria)
        .order_by(ItemEstoque.produto)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def listar_categorias(db: AsyncSession) -> list[str]:
    """Retorna lista de categorias únicas."""
    stmt = select(ItemEstoque.categoria).distinct().order_by(ItemEstoque.categoria)
    result = await db.execute(stmt)
    return list(result.scalars().all())
