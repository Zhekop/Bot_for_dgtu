from files.vars import dp
from aiogram import types, Router

router_get_photo = Router()

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def handle_photos(message: types.Message):
    # Получаем ID фотографий
    photo_ids = [photo.file_id for photo in message.photo]
    await message.answer(f"ID фотографий: {', '.join(photo_ids)}")
