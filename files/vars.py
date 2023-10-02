from time import strftime
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
#from gspread import *
from random import randint


TOKEN_API = '6175431771:AAHZt3Wk6BZCxWwB6V_n62wP0K89xhV2Kfg'
PROXY_URL = "http://proxy.server:3128"
#session = AiohttpSession(proxy=PROXY_URL)
# bot = Bot(token=TOKEN_API, session=session)
bot = Bot(TOKEN_API)
dp = Dispatcher()

now_time = strftime("%H:%M")  # время (NOW)
last_com = "@dgtu_yp11_bot"
Artem_ID = 998839766
Chat_Id_YP11 = -4068562450

answers = [
    ', ты не Артем((((',
    ', ты разве аретм?',
    ', ты же не артем, зачем ты сюда нажимаешь?',
    ', ладно'
]

def answer_for_artem(first_name, last_name):
    num = randint(0, 3)
    answer = answers[num]
    return f'{first_name} {last_name}{answer}'

async def good_morning(bot: Bot):
    await bot.send_message(Chat_Id_YP11, text = "Доброе утро моя стая!!")

async def good_night(bot: Bot):
    await bot.send_message(Chat_Id_YP11, text='Спокойной ночи моя стая!!')