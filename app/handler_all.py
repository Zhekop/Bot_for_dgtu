from gspread import Worksheet, Spreadsheet
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
# from files.vars import bot, Chat_Id_YP11, last_com

# router_all = Router()

# @router_all.message(Command('all', 'all'+last_com))
# async def call_all_members(message: Message):
#     if message.chat.id == Chat_Id_YP11:
#         for i in range(len(Users_of_grope)):
#             if Users_of_grope[i] == message.from_user.username:
#                 continue
#             else:
#                 await bot.send_message(Chat_Id_YP11, text=f'@{Users_of_grope[i]}')




def add_for_all(wh: Worksheet, msg: Message):
    main_wh = wh
    if msg.from_user.username == None:
        name = msg.from_user.first_name
    else:
        name = msg.from_user.username

    all_people = main_wh.get()

    for item in all_people:
        if item[0] == name:
            break
    else:
        main_wh.append_row([name])