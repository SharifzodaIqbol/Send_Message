from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
def key_board():
    button_key = KeyboardButton(text='Всем')
    button_1 = [button_key]
    markup = ReplyKeyboardMarkup(
        keyboard=[button_1],
        resize_keyboard=True,)
    return markup