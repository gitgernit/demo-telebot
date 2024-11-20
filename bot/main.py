import asyncio

import telebot.types

from bot.core import bot_router


@bot_router.message_handler(commands=['start'])
async def send_welcome(message: telebot.types.Message) -> None:
    text = 'Hello, World!'
    await bot_router.reply_to(message, text)


if __name__ == '__main__':
    asyncio.run(bot_router.polling())
