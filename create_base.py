import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from transparencia_solidaria.models import estoque_model
from transparencia_solidaria.core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)


def get_session() -> AsyncSession:
    _async_session: sessionmaker = sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        class_=AsyncSession,
        bind=engine,
    )

    session: AsyncSession = _async_session()
    return session


async def create_tables() -> None:
    async with engine.begin() as conn:
        print("Apagando tabelas...")
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        print("Criando tabelas...")
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas.")


if __name__ == "__main__":
    asyncio.run(create_tables())