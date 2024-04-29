from aiogram import Router, types
from aiogram.filters import Command

group_router = Router()


@group_router.message(Command("information"))
async def options_cad(message: types.Message):
    await message.answer(".... - ....")
