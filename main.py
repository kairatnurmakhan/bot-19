from aiogram.utils import executor
from config import dp
import logging
import asyncio

from handlers import client, extra, callback, admin, fsmAdminMenu, inline, notification
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
inline.register_handlers_inline(dp)
notification.register_handler_notification(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
