import enum


class Sorting(enum.StrEnum):
    NONE = 'none'
    FAVORITES = 'favorites'


class Headers(enum.StrEnum):
    CURRENT_PAGE = 'current_page'
    SWITCH_BACK = 'switch_back'
    SWITCH_FORTH = 'switch_forth'
    CHANGE_FILTER = 'change_filter'
    CRAFT = 'craft'
    ADD_TO_FAVORITES = 'add_to_favorites'
    DELETE_FROM_FAVORITES = 'delete_from_favorites'
