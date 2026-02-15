
import asyncio
import logging
import sys,os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv
from user import user,Menu

load_dotenv()
TOKEN = os.getenv("API")

if not TOKEN:
    raise ValueError("API yoq shu yerda xato")

logger=logging.getLogger(__name__)
xotira=MemoryStorage()
dp = Dispatcher(storage=xotira)


@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!,\n"
                         f"Menu tanlang.⏬",reply_markup=Menu)
async def main() -> None:
    logger.info("Bot ishga tushdi💯")
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    user(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
