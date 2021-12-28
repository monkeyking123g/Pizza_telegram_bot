from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #ReplyKeyboardRemove

b1 = KeyboardButton('/Orario_di_lavoro')
b2 = KeyboardButton('/Posizione')
b3 = KeyboardButton('/Menu')
#b4 = KeyboardButton('Numero di telefono', request_contact = True)
#b5 = KeyboardButton('Dove siamo ?', request_location = True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)#.row(b4, b5)