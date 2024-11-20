import asyncio

import telebot.async_telebot
import telebot.types

from bot.core.config import config

bot = telebot.async_telebot.AsyncTeleBot(config.TOKEN_TELEGRAM_API)


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message: telebot.types.Message) -> None:
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


@bot.message_handler(func=lambda message: message.text is not None)
async def echo_message(message: telebot.types.Message) -> None:
    await bot.reply_to(message, message.text)


if __name__ == '__main__':
    asyncio.run(bot.polling())
