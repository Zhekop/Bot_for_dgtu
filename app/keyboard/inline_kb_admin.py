from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel  = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Записать домашку",
            callback_data='make_homework'
        ),
        InlineKeyboardButton(
            text='Записать лекцию',
            callback_data='make_lecture'
        )
    ],
        [
        InlineKeyboardButton(
            text="Удалить домашку",
            callback_data='remove_homework'
        ),
        InlineKeyboardButton(
            text='Удалить лекцию',
            callback_data='remove_lecture'
        )
    ],
])