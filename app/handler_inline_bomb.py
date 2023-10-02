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


async def bomb(call:CallbackQuery):
    true_last_num = str(randint(1,4))
    True_call = f'call_{true_last_num}'
    try:
        if call.data == True_call:
            await call.message.answer(text=f'Молодец {call.from_user.first_name}, ты угадал')
            await bot.delete_message(call.message.chat.id, call.message.message_id)
        else:
            await call.answer(text='Блин, ты не угадал((((')
            await bot.delete_message(call.message.chat.id, call.message.message_id)
    except TelegramBadRequest:
        pass