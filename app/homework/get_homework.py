from files.vars import Chat_Id_YP11, sh, homeworks, index_homework
from gspread import Spreadsheet, Worksheet
from aiogram import Router
from aiogram.types import Message


def fill_zero_row(wh:Worksheet, msg:str):               #заполняет таблицу так
    sh_name = f"hw_{homeworks[index_homework(msg)]}"    #Название таблицы в файле
    wh = sh.worksheet(sh_name)                          #Объект Таблицы

    all_rows = wh.get_all_values()                      #Таблица с которой идет работа (все ее значения)
    index = 1
    for items in all_rows:
        if items[0] == '':
            pass
        index += 1
    
'''Доделать функцию'''


def add_homework(wh: Worksheet, message: Message):
    text = message.text.split('/')
    text = '123/123/123/123'.split("/")

