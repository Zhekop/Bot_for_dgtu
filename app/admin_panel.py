from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from files.vars import last_com, bot, admin_id
from app.keyboard.inline_kb_admin import admin_panel

router_admin = Router()

@router_admin.message(Command('admin', 'admin'+last_com))
async def admin(message: Message):
    message_id = message.message_id
    if message.from_user.id == admin_id:
        await bot.send_message(chat_id=message.from_user.id, text='Вот админ панель', reply_markup=admin_panel)
    await bot.delete_message(message.chat.id, message_id)
