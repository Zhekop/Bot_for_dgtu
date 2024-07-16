from gspread import Worksheet, Spreadsheet
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from files.vars import bot, Chat_Id_YP11, last_com, sh

router_all = Router()

@router_all.message(Command('all', 'all'+last_com))
async def call_all_members(message: Message):
    if message.chat.id == Chat_Id_YP11:
        wh = sh.worksheet('DGTU_Users')
        Users_of_grope = wh.get_all_values()
        for i in Users_of_grope:
            if i == message.from_user.username:
                continue
            else:
                await bot.send_message(Chat_Id_YP11, text=f'@{Users_of_grope[i]}')




def add_for_all(wh: Worksheet, msg: Message):
    if msg.from_user.username == None:
        name = msg.from_user.first_name
    else:
        name = msg.from_user.username

    all_people = wh.get()

    for item in all_people:
        if item[0] == name:
            break
    else:
        wh.append_row([name])