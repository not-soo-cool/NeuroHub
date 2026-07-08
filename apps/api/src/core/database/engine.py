from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from core.settings import get_settings

settings = get_settings()

engine: AsyncEngine = create_async_engine(
    settings.database.database_url.unicode_string(),
    echo=settings.app.debug,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=10,
)