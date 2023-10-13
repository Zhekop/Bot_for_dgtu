from aiogram import Router, F
from aiogram.types import Message

router_test = Router()

@router_test.message(F.photo)
async def handle_photos(message: Message):
# Получаем ID фотографий
#     photo_ids = [photo.file_id for photo in message.photo]
    
    # Собираем ID фотографий в одну строку
#     photo_ids_str = ', '.join(photo_ids)
    
    # Отправляем строку с ID фотографий пользователю
    # await message.answer(f"ID фотографий: {photo_ids_str}")
    await message.reply(text=message.photo[-1].file_id)


'''
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
'''