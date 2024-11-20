import telebot.types

from bot.apps.cards.enums import Headers
from bot.apps.cards.enums import Sorting


def get_personal_cards(
    card_id: int,
    page: int,
    amount: int,
    sorting: str | Sorting,
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
             (one of `bot.apps.cards.enums.Headers`) and key-values separated by spaces
    """

    buttons = [
        (
            telebot.types.InlineKeyboardButton(
                text=f'{page}/{amount}',
                callback_data=f'{Headers.CURRENT_PAGE} page:{page}',
            ),
            telebot.types.InlineKeyboardButton(
                text='>>',
                callback_data=f'{Headers.SWITCH_FORTH} page:{page} sorting:{sorting}',
            ),
        ),
        (
            telebot.types.InlineKeyboardButton(
                text='Сортировать',
                callback_data=f'{Headers.CHANGE_FILTER}',
            ),
        ),
        (
            telebot.types.InlineKeyboardButton(
                text='Крафт',
                callback_data=f'{Headers.CRAFT}',
            ),
        ),
        (
            telebot.types.InlineKeyboardButton(
                text='Добавить в избранное'
                if not favorite
                else 'Удалить из избранного',
                callback_data=f'{Headers.ADD_TO_FAVORITES if not favorite
                                 else Headers.DELETE_FROM_FAVORITES} card_id:{card_id}',
            ),
        ),
    ]

    if page > 1:
        buttons[0] = (
            telebot.types.InlineKeyboardButton(
                text='<<',
                callback_data=f'{Headers.SWITCH_BACK} page:{page} sorting:{sorting}',
            ),
        ) + buttons[0]

    keyboard = telebot.types.InlineKeyboardMarkup(buttons)

    return keyboard
