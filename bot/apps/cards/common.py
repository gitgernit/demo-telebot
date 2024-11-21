import sqlmodel.ext.asyncio.session

from bot.apps.cards import prompts
from bot.apps.cards.enums import Sorting
import bot.apps.cards.layouts
from bot.core import bot_router
from bot.core.config import ENGINE
import bot.models.card


async def send_personal_cards(
    *,
    chat_id: int,
    user_id: int,
    sorting: str | Sorting,
) -> None:
    async with sqlmodel.ext.asyncio.session.AsyncSession(
        ENGINE,
    ) as session:
        user: bot.models.user.User | None = await session.get(
            bot.models.user.User,
            user_id,
        )
        cards = await sort_cards(user.cards, 'none')

    page = 1 if cards else 0
    card_id = cards[page - 1].id if page else -1

    markup = bot.apps.cards.layouts.get_personal_cards_markup(
        amount=len(cards),
        card_id=card_id,
        page=page,
        sorting=sorting,
        favorite=False,
    )

    await bot_router.send_message(
        chat_id,
        text=prompts.CARD_DESCRIPTION.format(card_id=card_id)
        if card_id != 1
        else prompts.NO_CARDS,
        reply_markup=markup,
        parse_mode='HTML',
    )


async def sort_cards(
    cards: list[bot.models.card.Card],
    sorting: str | Sorting,
) -> list[bot.models.card.Card]:
    match sorting:
        case Sorting.NONE:
            return cards

        case _:
            raise NotImplementedError