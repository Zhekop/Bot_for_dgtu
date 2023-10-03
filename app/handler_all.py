from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from files.vars import bot, Chat_Id_YP11, Users_of_grope, last_com

router_all = Router()

@router_all.message(Command('all', 'all'+last_com))
async def call_all_members(message: Message):
    if message.chat.id == Chat_Id_YP11:
        for i in range(4):
            if Users_of_grope[i] == message.from_user.username:
                continue
            else:
                await bot.send_message(Chat_Id_YP11, text=f'@{Users_of_grope[i]}')