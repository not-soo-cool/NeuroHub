from functools import lru_cache

from core.config.ai import AISettings
from core.config.app import AppSettings
from core.config.database import DatabaseSettings
from core.config.redis import RedisSettings
from core.config.storage import StorageSettings


class Settings:
    def __init__(self) -> None:
        self.app = AppSettings()
        self.database = DatabaseSettings()
        self.redis = RedisSettings()
        self.storage = StorageSettings()
        self.ai = AISettings()


@lru_cache
def get_settings() -> Settings:
    return Settings()