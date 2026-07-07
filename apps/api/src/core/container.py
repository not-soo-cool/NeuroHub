from dataclasses import dataclass

from core.settings import Settings, get_settings


@dataclass(slots=True)
class AppContainer:
    settings: Settings

    # Will be initialized later
    db_engine: object | None = None
    redis: object | None = None
    qdrant: object | None = None
    s3: object | None = None


container = AppContainer(
    settings=get_settings(),
)