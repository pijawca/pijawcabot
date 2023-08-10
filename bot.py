# -*- coding: utf-8 -*-
#!/usr/bin/env python
from aiogram import executor
from aiogram.dispatcher import Dispatcher
from misc import dp
from handlers import general
from db import create_table

general.register_handlers_commands(dp)
async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == "__main__":
    create_table()
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown) 