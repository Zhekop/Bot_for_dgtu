from aiogram.types import CallbackQuery
from files.vars import Artem_ID, answer_for_artem

async def artem(call: CallbackQuery):
    if call.from_user.id == Artem_ID:
        await call.message.answer(text = 'Будь умничкой и учись, пары прогуливать нельзя')
    else:
        print(call.data)
        await call.answer(text = answer_for_artem(call.from_user.first_name, call.from_user.last_name))
