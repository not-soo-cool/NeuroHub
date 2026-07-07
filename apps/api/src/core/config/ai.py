from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AISettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    openai_api_key: SecretStr = Field(..., alias="OPENAI_API_KEY")
    anthropic_api_key: SecretStr = Field(..., alias="ANTHROPIC_API_KEY")
    google_api_key: SecretStr = Field(..., alias="GOOGLE_API_KEY")