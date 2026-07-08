from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.container import container
from core.database.engine import engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Application startup.
    """

    # In upcoming sprints:
    # - Create SQLAlchemy engine
    # - Initialize Redis
    # - Initialize Qdrant
    # - Initialize MinIO

    app.state.container = container
    container.db_engine = engine

    yield

    """
    Application shutdown.
    """

    # Dispose resources here
    await engine.dispose()