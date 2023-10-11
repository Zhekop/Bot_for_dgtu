from aiogram import Router, F
from aiogram.types import Message

router_test = Router()

@router_test.message(F.photo)
async def send_caption(message: Message):
    photos = message.photo[-1].file_id
    for photo in photos:
        await message.answer(text=photo)    
    # list_a = [message.photo[-1].file_id]
    # strng = ''
    # for i in list_a:
    #     strng = strng + i + '\n'
    # print(strng)
    # await message.answer(strng)