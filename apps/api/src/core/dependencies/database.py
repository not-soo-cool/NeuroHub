from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.session import get_db


async def get_database() -> AsyncGenerator[AsyncSession, None]:
    async for session in get_db():
        yield session