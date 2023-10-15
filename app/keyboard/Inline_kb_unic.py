from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_universiti = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Покажи домашку",
            callback_data='show_homework'
        ),
        InlineKeyboardButton(
            text='Покажи лекцию',
            callback_data='show_lecture'
        )
    ],
    [
        InlineKeyboardButton(
            text='артем, нажми',
            callback_data='artem'
        )
    ],
    [
        InlineKeyboardButton(
            text='расписание',
            #callback_data='lesson_schedule'
            url = 'https://edu.donstu.ru/WebApp/#/Rasp/Group/50918'
        )
    ]
])