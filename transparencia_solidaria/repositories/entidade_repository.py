from sqlalchemy import select, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from transparencia_solidaria.models.estoque_model import Entidade, Cidade, Estado


async def listar_entidades(
    db: AsyncSession,
    estado_sigla: str | None = None,
    cidade_nome: str | None = None,
    ordenar_por: str = "nome",
    ordem: str = "asc",
    skip: int = 0,
    limit: int = 20,
) -> list[Entidade]:
    stmt = (
        select(Entidade)
        .join(Entidade.cidade)
        .join(Cidade.estado)
        .options(selectinload(Entidade.cidade).selectinload(Cidade.estado))
    )

    if estado_sigla:
        stmt = stmt.where(Estado.sigla == estado_sigla.upper())

    if cidade_nome:
        stmt = stmt.where(Cidade.nome.ilike(f"%{cidade_nome}%"))

    colunas_validas = {"nome", "fundacao", "criado_em"}
    col = ordenar_por if ordenar_por in colunas_validas else "nome"
    col_attr = getattr(Entidade, col)
    stmt = stmt.order_by(asc(col_attr) if ordem == "asc" else desc(col_attr))

    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def listar_estados(db: AsyncSession) -> list[Estado]:
    result = await db.execute(select(Estado).order_by(Estado.nome))
    return list(result.scalars().all())


async def listar_cidades(
    db: AsyncSession,
    estado_sigla: str | None = None,
) -> list[Cidade]:
    stmt = select(Cidade).join(Cidade.estado).options(selectinload(Cidade.estado))
    if estado_sigla:
        stmt = stmt.where(Estado.sigla == estado_sigla.upper())
    stmt = stmt.order_by(Cidade.nome)
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def buscar_entidade_por_id(
    db: AsyncSession,
    entidade_id: int,
) -> Entidade | None:
    stmt = (
        select(Entidade)
        .where(Entidade.id == entidade_id)
        .options(selectinload(Entidade.cidade).selectinload(Cidade.estado))
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()
