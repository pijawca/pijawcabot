# -*- coding: utf-8 -*-
# -8- pijawca -8-
from aiogram import executor
from aiogram.dispatcher import Dispatcher
from misc import dp
from handlers import general

general.register_handlers_commands(dp)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
