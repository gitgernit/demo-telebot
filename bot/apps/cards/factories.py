import telebot.callback_data

from bot.apps.cards.enums import Headers
from bot.apps.cards.enums import Sorting


class CardListCallbackFactory:
    def __init__(
        self,
        fields: tuple[str] = (
            'amount',
            'card_id',
            'sorting',
            'page',
            'favorite',
        ),
    ) -> None:
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


class SortingListCallbackFactory:
    def __init__(self) -> None:
        self.none = telebot.callback_data.CallbackData(prefix=Sorting.NONE)
        self.sorted = telebot.callback_data.CallbackData(prefix=Sorting.FAVORITES)

        self.all_factories: tuple[telebot.callback_data.CallbackData] = (
            self.none, self.sorted,
        )


card_list_callback_factory = CardListCallbackFactory()
sorting_list_callback_factory = SortingListCallbackFactory()
