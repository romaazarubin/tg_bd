from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton

menu_application = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Ответить', callback_data='answer')
            ]
        ]
    )

button_client_help = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Написать менеджеру', callback_data='help')
        ]
    ]
)

button_sity = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Москва', callback_data='Moskva')
        ],
        [
            InlineKeyboardButton(text='СПБ', callback_data='spb')
        ],
        [
            InlineKeyboardButton(text='Иркутск', callback_data='Irkutsk')
        ]
    ]
)