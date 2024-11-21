import sqlmodel.ext.asyncio.session
import telebot.types

import bot.apps.cards.common
import bot.apps.cards.enums
import bot.apps.cards.layouts
from bot.core import bot_router
from bot.core.config import ENGINE
import bot.models.card
import bot.models.user


@bot_router.message_handler(commands=['my_cards'])
async def get_personal_cards_by_message(
    message: telebot.types.Message,
) -> None:
    await bot.apps.cards.common.send_personal_cards(
        chat_id=message.chat.id,
        user_id=message.from_user.id,
        sorting=bot.apps.cards.enums.Sorting.NONE,
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
