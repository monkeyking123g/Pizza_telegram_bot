from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #ReplyKeyboardRemove


button_load = KeyboardButton('/Caricare')
button_delete = KeyboardButton('/cancellare')
button_exit = KeyboardButton('exit')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete).add(button_exit)