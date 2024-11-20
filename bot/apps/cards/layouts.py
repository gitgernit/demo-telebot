import telebot.types

from bot.apps.cards.enums import Sorting
from bot.apps.cards.factories import CallbackFactory


def get_personal_cards(
    *,
    amount: int,
    card_id: int,
    sorting: str | Sorting,
    page: int,
    favorite: bool,
) -> telebot.types.InlineKeyboardMarkup:
    """
    Get an inline keyboard for personal cards

    :param card_id: Card's UUID
    :param page: Current page
    :param amount: Total amount of pages
    :param sorting: One of `bot.apps.cards.enums.Sorting`
    :param favorite: Whether the card is favorite or not
    :return: Corresponding inline keyboard with callback data being a header
             (one of `bot.apps.cards.enums.Headers`) and corresponding
             fields from `bot.apps.cards.factories.callback_factory.fields`
    """
    callback_factory = CallbackFactory(
        dict(
            amount=amount,
            card_id=card_id,
            sorting=sorting,
            page=page,
            favorite=favorite,
        ),
    )

    buttons = [
        (
            telebot.types.InlineKeyboardButton(
                text=f'{page}/{amount}',
                callback_data=callback_factory.craft.new(
                    **callback_factory.fields,
                ),
            ),
            telebot.types.InlineKeyboardButton(
                text='>>',
                callback_data=callback_factory.switch_forth.new(
                    **callback_factory.fields,
                ),
            ),
        ),
        (
            telebot.types.InlineKeyboardButton(
                text='Сортировать',
                callback_data=callback_factory.change_filter.new(
                    **callback_factory.fields,
                ),
            ),
        ),
        (
            telebot.types.InlineKeyboardButton(
                text='Крафт',
                callback_data=callback_factory.craft.new(
                    **callback_factory.fields,
                ),
            ),
        ),
        (
            telebot.types.InlineKeyboardButton(
                text='Добавить в избранное'
                if not favorite
                else 'Удалить из избранного',
                callback_data=callback_factory.add_to_favorites.new(
                    **callback_factory.fields,
                ),
            ),
        ),
    ]

    if page > 1:
        buttons[0] = (
            telebot.types.InlineKeyboardButton(
                text='<<',
                callback_data=callback_factory.switch_back.new(
                    **callback_factory.fields,
                ),
            ),
        ) + buttons[0]

    return telebot.types.InlineKeyboardMarkup(buttons)
