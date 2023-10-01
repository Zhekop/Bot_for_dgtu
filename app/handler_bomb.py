from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message #, CallbackQuery
from files.vars import last_com
from random import randint

router_bomb = Router()

@router_bomb.message(Command('info', 'info'+last_com))
async def bomb():
    pass