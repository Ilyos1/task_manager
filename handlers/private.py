from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from keyboards.for_navigate import keyboard

private_router = Router()

@private_router.message(CommandStart())
async def start_сcd(message: types.Message):
    await message.answer("start", reply_markup=keyboard)


@private_router.message(Command("options"))
async def options_cad(message: types.Message):
    await message.answer("optional list")
