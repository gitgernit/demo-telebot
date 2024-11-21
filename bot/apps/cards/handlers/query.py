import sqlmodel.ext.asyncio.session
import telebot.types

from bot.apps.cards import prompts
import bot.apps.cards.common
from bot.apps.cards.factories import callback_factory
import bot.apps.cards.layouts
from bot.core import bot_router
from bot.core.config import ENGINE
import bot.models.user


@bot_router.callback_query_handler(
    func=lambda query: callback_factory.switch_forth.filter().check(query),
)
async def switch_forth(call: telebot.types.CallbackQuery) -> None:
    data = callback_factory.switch_forth.parse(call.data)
    await switch_by_callback(call=call, data=data, positive=True)


@bot_router.callback_query_handler(
    func=lambda query: callback_factory.switch_back.filter().check(query),
)
async def switch_back(call: telebot.types.CallbackQuery) -> None:
    data = callback_factory.switch_back.parse(call.data)
    await switch_by_callback(call=call, data=data, positive=False)


async def switch_by_callback(
    *,
    call: telebot.types.CallbackQuery,
    data: dict[str, str],
    positive: bool,
) -> None:
    async with sqlmodel.ext.asyncio.session.AsyncSession(
        ENGINE,
    ) as session:
        user: bot.models.user.User | None = await session.get(
            bot.models.user.User,
            call.from_user.id,
        )
        cards = await bot.apps.cards.common.sort_cards(
            user.cards,
            data['sorting'],
        )

    direction = 1 if positive else -1
    page = min(int(data['page']) + direction, len(cards))
    card_id = int(cards[page - 1].id) if cards else -1

    markup = bot.apps.cards.layouts.get_personal_cards(
        amount=len(cards),
        card_id=card_id,
        page=page,
        sorting=data['sorting'],
        favorite=False,
    )

    await bot_router.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.id,
        text=prompts.CARD_DESCRIPTION.format(card_id=card_id)
        if card_id != 1
        else prompts.NO_CARDS,
        reply_markup=markup,
        parse_mode='HTML',
    )
