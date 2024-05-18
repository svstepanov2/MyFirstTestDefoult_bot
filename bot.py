import os
import re
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="7182065332:AAHbTKDrR89wF3pARSfoiS-A6oaEwvdz9Nc")
dp = Dispatcher(bot, storage=MemoryStorage())

async def echo_command(message: types.Message):
    if message.text.startswith("/user"):
        await message.answer(f"User: {message.from_user.full_name}")

    elif message.text.startswith("/info"):
        await message.answer(f"Info: Here is some generic bot info.")

@dp.message_handler(commands=["echo"])
async def echo_command_handler(message: types.Message):
    await echo_command(message)

@dp.message_handler(commands=["user", "info"])
async def command_handler(message: types.Message):
    await message.answer(f"Command: {message.text}")
    await echo_command(message)

if __name__ == "__main__":
    dp.run_polling()