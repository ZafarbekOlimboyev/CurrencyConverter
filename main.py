import sys
from config import TOKEN
from aiogram import Bot, Dispatcher
import asyncio
import logging
from hendlers.cmd_c import cmd_co
from hendlers.msg_c import msg_co


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(cmd_co, msg_co)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())