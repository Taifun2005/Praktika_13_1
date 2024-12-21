from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# def keyboardButton(text):
#     pass


stat_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость"),
            KeyboardButton(text="О нас")

        ]
    ], resize_keyboard=True
)
katalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Средняя игра',callback_data="medium")],
        [InlineKeyboardButton(text='Большая игра',callback_data="big")],
        [InlineKeyboardButton(text='Очень большая игра',callback_data="mega")],
        [InlineKeyboardButton(text='Другие предложения',callback_data="other")]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        InlineKeyboardButton(text='Купить!', url='https://bing.com')
    ]
)