from files.vars import dp
from aiogram import types, Router, F

router_get_photo = Router()

@dp.message_handler(F.photo)
async def handle_photos(message: types.Message):
    # Получаем ID фотографий
    photo_ids = [photo.file_id for photo in message.photo]
    await message.answer(f"ID фотографий: {', '.join(photo_ids)}")
