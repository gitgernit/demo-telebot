__all__: list[str] = []

# Trigger apps initialization
# Tinkering with asyncio's event loop for sqlalchemy compatibility
import asyncio
import sys

import bot.apps

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
