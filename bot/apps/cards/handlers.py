import telebot.types

from bot.apps.cards.layouts import get_personal_cards
from bot.core import bot_router


@bot_router.message_handler(commands=['my_cards'])
async def send_user_cards(message: telebot.types.Message) -> None:
    markup = get_personal_cards(
        card_id=0,
        page=2,
        amount=50,
        sorting='favorites',
        favorite=True,
    )
    await bot_router.reply_to(message, 'Some cards', reply_markup=markup)
