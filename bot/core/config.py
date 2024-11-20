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


config = Config()
