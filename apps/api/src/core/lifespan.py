from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.container import container


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

    yield

    """
    Application shutdown.
    """

    # Dispose resources here