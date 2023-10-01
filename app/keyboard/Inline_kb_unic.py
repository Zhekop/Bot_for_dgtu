from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_universiti = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Домашка",
            callback_data='homework'
        ),
        InlineKeyboardButton(
            text='Лекция',
            callback_data='lecture_show'
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