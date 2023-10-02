from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app.keyboard.Inline_kb_unic import select_universiti
from files.vars import last_com, Artem_ID, answer_for_artem, bot

router_inline = Router()

@router_inline.message(Command('unic', 'unic'+last_com))
async def get_kb_inline_universiti(message: Message):
    await message.answer(
        text='выбирай друже', 
        reply_markup=select_universiti
        )


async def artem(call: CallbackQuery):
    if call.from_user.id == Artem_ID:
        await call.message.answer(text = 'Будь умничкой и учись, пары прогуливать нельзя')
    else:
        await call.answer(text = answer_for_artem(
            call.from_user.first_name, call.from_user.last_name))

