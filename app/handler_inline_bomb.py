from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app.keyboard.inline_kb_bomb import select_bomb
from files.vars import last_com,  bot
from random import randint



router_bomb = Router()

@router_bomb.message(Command('bomb', 'bomb'+last_com))
async def get_kb_inline_bomb(message: Message):
    message_id = message.message_id
    await bot.send_message(
        chat_id=message.chat.id,
        text='выбери один из проводов',
        reply_markup=select_bomb
    )   
    await bot.delete_message(message.chat.id, message_id)


