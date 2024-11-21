import sqlmodel.ext.asyncio.session
import telebot.types

import bot.apps.cards.common
import bot.apps.cards.layouts
from bot.core import bot_router
from bot.core.config import ENGINE
import bot.models.card
import bot.models.user


@bot_router.message_handler(commands=['my_cards'])
async def send_user_cards(message: telebot.types.Message) -> None:
    async with sqlmodel.ext.asyncio.session.AsyncSession(
        ENGINE,
    ) as session:
        user: bot.models.user.User | None = await session.get(
            bot.models.user.User,
            message.from_user.id,
        )
        cards = await bot.apps.cards.common.sort_cards(user.cards, 'none')

    page = 1 if cards else 0
    card_id = cards[page - 1].id if page else -1

    markup = bot.apps.cards.layouts.get_personal_cards(
        amount=len(cards),
        card_id=card_id,
        page=page,
        sorting='none',
        favorite=False,
    )

    await bot_router.reply_to(
        message,
        f'Card id: <b>{card_id}</b>'
        if card_id != -1
        else "You've got none :(",
        reply_markup=markup,
        parse_mode='HTML',
    )


@bot_router.message_handler(commands=['get_card'])
async def generate_card(message: telebot.types.Message) -> None:
    async with sqlmodel.ext.asyncio.session.AsyncSession(
        ENGINE,
    ) as session:
        card = bot.models.card.Card(
            user_id=message.from_user.id,
        )

        session.add(card)
        await session.commit()


@bot_router.message_handler(commands=['delete_card'])
async def delete_card(message: telebot.types.Message) -> None:
    async with sqlmodel.ext.asyncio.session.AsyncSession(
        ENGINE,
    ) as session:
        user: bot.models.user.User | None = await session.get(
            bot.models.user.User,
            message.from_user.id,
        )

        if user.cards:
            await session.delete(user.cards[0])
            await session.commit()
