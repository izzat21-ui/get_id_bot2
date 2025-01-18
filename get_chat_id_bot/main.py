import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy import select, insert
from sqlalchemy.orm import sessionmaker

from config import engine
from get_chat_id_bot.models import User

TOKEN = "7752592433:AAE7uxFnle0Q50hC4YmTz5k_GBPD75iKGzY"

dp = Dispatcher()
session = sessionmaker(engine)()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    query = select(User).where(User.chat_id==message.from_user.id)
    result =  session.execute(query).fetchone()
    user = message.from_user
    if not result:
        query = insert(User).values(chat_id= user.id ,
                                    first_name=user.first_name ,
                                    last_name=user.last_name,
                                    username=user.username)
        session.execute(query)
        session.commit()
    await message.answer(f"Uxladiz jigarim, {html.bold(message.from_user.full_name)}!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
