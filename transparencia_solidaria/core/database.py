from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from transparencia_solidaria.core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=False)


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
    print("Pronto!")


from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from transparencia_solidaria.core.configs import settings

# Engine assíncrono para PostgreSQL via asyncpg
_engine = create_async_engine(
    settings.DB_URL,
    echo=False,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)

_AsyncSessionLocal = async_sessionmaker(
    bind=_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency FastAPI: fornece uma sessão async do banco."""
    async with _AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
