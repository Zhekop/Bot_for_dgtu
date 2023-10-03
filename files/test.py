# from vars import last_com
# command = '/info'
# print(command+last_com)

# import random
# a = ['0', '1', '2', '3']
# num = random.randint(1, 4)
# for i in range(1, 14):
#     num = random.randint(0, 3)
#     print(num)



async def bomb(call:CallbackQuery):
    true_last_num = str(randint(1,4))
    True_call = f'call_{true_last_num}'
    try:
        if call.data == True_call:
            await call.message.answer(text=f'Молодец {call.from_user.first_name}, ты угадал')
            await bot.delete_message(call.message.chat.id, call.message.message_id)
        else:
            await call.answer(text='Блин, ты не угадал((((')
            await bot.delete_message(call.message.chat.id, call.message.message_id)
    except TelegramBadRequest:
        pass