import sqlmodel
import sqlmodel.ext.asyncio.session
import telebot.asyncio_handler_backends
import telebot.types

from bot.core import bot_router
from bot.core.config import ENGINE
import bot.models.card
import bot.models.user


class RegisterUserMiddleware(telebot.asyncio_handler_backends.BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()
        self.update_sensitive = True
        self.update_types = ['message', 'callback_query']

    async def pre_process_message(
        self,
        message: telebot.types.Message,
        data: dict,
    ) -> None:
        user_id = message.from_user.id
        await self.register_user(user_id=user_id)

    async def post_process_message(
        self,
        message: telebot.types.Message,
        data: dict,
        exception: Exception,
    ) -> None:
        pass

    async def pre_process_callback_query(
        self,
        call: telebot.types.CallbackQuery,
        data: dict,
    ) -> None:
        user_id = call.from_user.id
        await self.register_user(user_id=user_id)

    async def post_process_callback_query(
        self,
        call: telebot.types.CallbackQuery,
        data: dict,
        exception: Exception,
    ) -> None:
        pass

    async def register_user(self, *, user_id: int) -> None:
        async with sqlmodel.ext.asyncio.session.AsyncSession(
            ENGINE,
        ) as session:
            if not await session.get(
                bot.models.user.User,
                user_id,
            ):
                user = bot.models.user.User(
                    id=user_id,
                )

                session.add(user)
                await session.commit()


bot_router.setup_middleware(RegisterUserMiddleware())
