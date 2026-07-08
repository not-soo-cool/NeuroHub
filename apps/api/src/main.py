from fastapi import FastAPI, Depends

from core.lifespan import lifespan
from core.container import AppContainer
from core.dependencies.container import get_container

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import get_database

app = FastAPI(
    title="NeuroHub API",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "api",
    }
    
@app.get("/info")
async def info(
    container: AppContainer = Depends(get_container),
):
    return {
        "app": container.settings.app.app_name,
        "environment": container.settings.app.app_env,
    }

@app.get("/db/health")
async def db_health(
    db: AsyncSession = Depends(get_database),
):
    result = await db.execute(text("SELECT 1"))
    return {"database": result.scalar_one() == 1}