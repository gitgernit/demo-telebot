__all__: list[str] = ['bot_router']

import telebot.async_telebot

from bot.core.config import config


class ExceptionHandler(telebot.ExceptionHandler):
    def handle(self, exception: Exception) -> None:
        raise exception


bot_router = telebot.async_telebot.AsyncTeleBot(
    config.TOKEN_TELEGRAM_API,
    exception_handler=ExceptionHandler(),
)
