from files.vars import Chat_Id_YP11, sh, homeworks, index_homework
from gspread import Spreadsheet, Worksheet
from aiogram import Router
from aiogram.types import Message
from aiogram import F

def add_homework(wh: Worksheet, list_hw: list):  #заполняет таблицу так    
    all_rows = wh.get_all_values()                          #Таблица с которой идет работа (все ее значения)
    index = 1
    for items in all_rows:
        if items[0] == '':
            pass
            break
        index += 1
    else:
        wh.append_row()

router_get_hw = Router()

@router_get_hw.message(F.photo)
async def get_homework(message: Message):
    subj = index_homework(message.caption.lower())
    date = message.text.replace(subj[1], '').replace(' ', '')
    wh_name = f'hw_{subj[0]}'
    worksheet = sh.worksheet(wh_name)
    data_for_wh = [date,]
    add_homework(wh=worksheet, list_wh=data_for_wh)




    
'''Доделать функцию'''



