from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from app.keyboard.Inline_kb_unic import select_universiti
from files.vars import last_com

router_inline = Router()

@router_inline.message(Command('unic', 'unic'+last_com))
async def get_kb_inline_universiti(message: Message):
    await message.answer(
        text='выбирай друже', 
        reply_markup=select_universiti
        )
