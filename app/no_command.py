from files.vars import bot, Chat_Id_YP11, akim_photo_id_yes, akim_photo_id_no, admin_id
from aiogram import Router, F
from aiogram.types import Message
from random import randint



router_no_command = Router()

@router_no_command.message(F.text)
async def send_text_no_command(message: Message):
    if 'негр' in message.text.lower():
        await bot.send_message(chat_id=message.chat.id, text='8 ши')
    elif 'бот' in message.text.lower():
        if message.from_user.id == admin_id:
            await message.reply(text='Вы не бот')
        else:
            await bot.send_message(chat_id=message.chat.id, text='Сам бот')
    elif 'смешарик' in message.text.lower():
        num = randint(1,2)
        if num == 1:
            await message.reply_photo(photo=akim_photo_id_yes, caption='Ты смешарик')
        else:
            await message.reply_photo(photo=akim_photo_id_no, caption='Ты не смешарик')



''' 
негр = 8 ши 
бот = сам бот
смешарик = фото акима (на его выбор)
''' 