from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_universiti = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='1',
            callback_data='call_1'
        ),
        InlineKeyboardButton(
            text='2',
            callback_data='call_2'
        )
    ],
    [
        InlineKeyboardButton(
            text='3',
            callback_data='call_3'
        ),
        InlineKeyboardButton(
            text='4',
            callback_data='call_4'
        )
    ],
])