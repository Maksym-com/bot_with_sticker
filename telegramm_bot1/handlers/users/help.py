from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/saysomethink - Розказати цитату",
            "/start - Начать диалог",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))
