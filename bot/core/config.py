import pathlib

import pydantic
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=pathlib.Path(__file__).parent.parent.parent / '.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    TOKEN_TELEGRAM_API: str = pydantic.fields.Field(default=None)
    DEBUG: bool = pydantic.fields.Field(default=False)

    POSTGRES_HOST: str = pydantic.fields.Field(default=None)
    POSTGRES_PORT: str = pydantic.fields.Field(default=None)
    POSTGRES_DB: str = pydantic.fields.Field(default=None)
    POSTGRES_USER: str = pydantic.fields.Field(default=None)
    POSTGRES_PASSWORD: str = pydantic.fields.Field(default=None)


config = Config()

DB_URL = f'postgresql+psycopg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}'
