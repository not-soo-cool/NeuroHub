from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class StorageSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    endpoint: str = Field(..., alias="S3_ENDPOINT")
    access_key: str = Field(..., alias="S3_ACCESS_KEY")
    secret_key: str = Field(..., alias="S3_SECRET_KEY")
    bucket_name: str = Field(..., alias="S3_BUCKET")