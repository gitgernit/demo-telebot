import telebot.types

from bot.apps.cards.layouts import get_personal_cards
from bot.core import bot_router


@bot_router.message_handler(commands=['my_cards'])
async def send_user_cards(message: telebot.types.Message) -> None:
    markup = get_personal_cards(0, 2, 50, 'favorites', True)
    await bot_router.reply_to(message, 'Some cards', reply_markup=markup)
