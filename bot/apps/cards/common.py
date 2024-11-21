from bot.apps.cards.enums import Sorting
import bot.models.card


async def sort_cards(
    cards: list[bot.models.card.Card],
    sorting: str | Sorting,
) -> list[bot.models.card.Card]:
    match sorting:
        case Sorting.NONE:
            return cards

        case _:
            raise NotImplementedError
