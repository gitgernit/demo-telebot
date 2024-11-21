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
        self.update_types = telebot.util.update_types

    async def pre_process(
        self,
        message: telebot.types.Message,
        data: dict,
    ) -> None:
        async with sqlmodel.ext.asyncio.session.AsyncSession(
            ENGINE,
        ) as session:
            if not await session.get(
                bot.models.user.User,
                message.from_user.id,
            ):
                user = bot.models.user.User(
                    id=message.from_user.id,
                )

                session.add(user)
                await session.commit()

    async def post_process(
        self,
        message: telebot.types.Message,
        data: dict,
        exception: Exception,
    ) -> None:
        pass


bot_router.setup_middleware(RegisterUserMiddleware())
