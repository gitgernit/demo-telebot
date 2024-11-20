import typing

import telebot.callback_data

from bot.apps.cards.enums import Headers


class CallbackFactory:
    def __init__(self, fields: dict[str, typing.Any]) -> None:
        self.fields = fields

        self.switch_back = telebot.callback_data.CallbackData(
            *fields,
            prefix=Headers.SWITCH_BACK,
        )
        self.current_page = telebot.callback_data.CallbackData(
            *fields,
            prefix=Headers.CURRENT_PAGE,
        )
        self.switch_forth = telebot.callback_data.CallbackData(
            *fields,
            prefix=Headers.SWITCH_FORTH,
        )
        self.change_filter = telebot.callback_data.CallbackData(
            *fields,
            prefix=Headers.CHANGE_FILTER,
        )
        self.craft = telebot.callback_data.CallbackData(
            *fields,
            prefix=Headers.CRAFT,
        )
        self.add_to_favorites = telebot.callback_data.CallbackData(
            *fields,
            prefix=Headers.ADD_TO_FAVORITES,
        )
        self.delete_from_favorites = telebot.callback_data.CallbackData(
            *fields,
            prefix=Headers.DELETE_FROM_FAVORITES,
        )
