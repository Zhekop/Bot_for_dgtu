from aiogram import Router
from aiogram.types import ContentType, Message
from files.vars import bot, dp

router_new_member = Router()

@router_new_member.chat_join_request(content_types=[ContentType.NEW_CHAT_MEMBERS])
async def new_members_handler(message: Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=f"Добро пожаловать, {message.from_user.first_name}")