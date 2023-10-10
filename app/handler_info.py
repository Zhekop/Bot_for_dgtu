from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message #, CallbackQuery
from files.vars import last_com

router_info = Router()

@router_info.message(Command('info', 'info@KruHelper_bot'))
async def info(message: Message):
    # await message.answer(text=f"username - {message.from_user.username}")
    # await message.answer(text=f"{message}")
    # print(message)
    await message.answer(text=f"Чат ID - {message.chat.id}")
    await message.answer(text=f"Юзер ID - {message.from_user.id}")
    # await message.answer(message.text)
    # await message.answer(message.photo[-1].file_id)



