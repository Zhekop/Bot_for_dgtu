# from aiogram import F, Router
# from aiogram.filters import Command
# from aiogram.types import Message
# from files.vars import bot, Chat_Id_YP11, last_com

# router_test = Router()

# @router_test.message(Command('test', 'test'+last_com))
# async def test(message: Message):
#     if (message.from_user.first_name not in Users_of_grope) and (message.from_user.username not in Users_of_grope):
#         if message.from_user.username == None:
#             print(f'"{message.from_user.first_name}",')
#         else:
#             print(f'"{message.from_user.username}",')
#     else:
#         pass