from time import strftime
from aiogram import Bot, Dispatcher
from aiogram.types import Message
# from aiogram.client.session.aiohttp import AiohttpSession
from gspread import Client, service_account, Spreadsheet
from random import randint

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1wo5WAXwuooCooOPMYcFXkN0MrvGPcAiasYtWlX9Pa9A/edit#gid=0"
gc: Client = service_account("./files/.service_account.json")   #Подключение к акку который может редачить табицу
sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)               #Объект файла

TOKEN_API = '6175431771:AAHZt3Wk6BZCxWwB6V_n62wP0K89xhV2Kfg'
PROXY_URL = "http://proxy.server:3128"
#session = AiohttpSession(proxy=PROXY_URL)
# bot = Bot(token=TOKEN_API, session=session)
bot = Bot(TOKEN_API)
dp = Dispatcher()

now_time = strftime("%H:%M")  # время (NOW)

last_com = "@dgtu_yp11_bot"

akim_photo_id_yes = 'AgACAgIAAx0Cc7N-pAACAptlKQ_UwpBLIs7nNdeTZh2qJsetGgACcswxG3qHSEnAmu4lkxmLSAEAAwIAA3kAAzAE'
akim_photo_id_no = 'AgACAgIAAx0Cc7N-pAACAq1lKRMl5eAz-u20VXQkgkuQdDa7QwACbdExG4IESEmFqvSzHERAnQEAAwIAA3kAAzAE'
Artem_ID = 998839766
admin_id = 1016825585   
Chat_Id_YP11 = -1001941143204
Test_chat_id = -1001841963988

answers = {
    ', ты не Артем((((',
    ', ты разве аретм?',
    ', ты же не артем, зачем ты сюда нажимаешь?',
    ', ладно'
}


def index_homework(msg:str) -> list:
    match msg:
        case msg if 'мат' in msg : return ["math", "мат"]
        case msg if 'ист' in msg : return ["history", "ист"]
        case msg if 'анг' in msg : return ["english", "анг"]
        case msg if 'инф' in msg : return ["informatic", "инф"]
        case msg if 'хим' in msg : return ["chemistry", "хим"]

def answer_for_artem(first_name, last_name) -> str:
    num = randint(0, 3)
    answer = answers[num]
    return f'{first_name} {last_name}{answer}'


async def good_morning(bot: Bot) -> None:
    await bot.send_message(Chat_Id_YP11, text = "Доброе утро моя стая!!")

async def good_night(bot: Bot) -> None:
    await bot.send_message(Chat_Id_YP11, text = 'Спокойной ночи Артемчик, учись хорошшо и не прогуливай!!')

async def get_photo(message: Message) -> None:
    await message.answer(message.photo[-1].file_id)


class Input_Homework:
    def __init__(self, date:str, subject:str, list_img:list, bot:Bot = bot) -> None:
        self.date: str = date
        self.subject: str = subject
        self.list_img: list = list_img
        self.bot = bot
