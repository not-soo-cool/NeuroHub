from fastapi import FastAPI, Depends

from core.lifespan import lifespan
from core.container import AppContainer
from core.dependencies.container import get_container

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