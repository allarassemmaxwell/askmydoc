from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

# ========================
# Database Engine
# ========================

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,   # logs all SQL queries in development
    pool_size=10,          # max 10 persistent connections
    max_overflow=20,       # 20 extra connections allowed under heavy load
    pool_pre_ping=True,    # test connection before using it
)

# ========================
# Session Factory
# ========================

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# ========================
# Base Model Class
# ========================

class Base(DeclarativeBase):
    """
    All database models inherit from this class.
    SQLAlchemy uses it to know which classes are DB tables.
    """
    pass


# ========================
# Dependency — used in routes
# ========================

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Creates a new database session for each request.
    Automatically commits or rolls back and closes when done.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()