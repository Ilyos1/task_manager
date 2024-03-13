import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="7125278630:AAHnY1pzQKY9llJdT_pL0j1XkwTlEkKG40k")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_ccd(message: types.Message):
    await message.answer("staaart")


@dp.message()
async def echo(message: types.Message):
    await message.answer("echo echo")


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
