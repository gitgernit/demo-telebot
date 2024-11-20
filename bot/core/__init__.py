__all__: list[str] = ['bot_router']

import logging
import traceback

import telebot.async_telebot

from bot.core.config import config


class ExceptionHandler(telebot.ExceptionHandler):
    def handle(self, exception):
        raise exception


bot_router = telebot.async_telebot.AsyncTeleBot(
    config.TOKEN_TELEGRAM_API, exception_handler=ExceptionHandler()
)
