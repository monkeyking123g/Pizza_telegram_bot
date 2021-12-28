from aiogram import types, Dispatcher 
from create_bot import dp, bot
from data_base import sqlite_db 
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db 

"""***************************Parte Clienti**********************"""
#@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Buon appetito', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Per parlare con PzzaBot scrivi in privato:\nhttps://t.me/Pizza_Pizzaxbot')

#@dp.message_handler(commands=['orario_di_lavoro'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'aperto da Ln-Sb dalle 9:00 alle 22:00')

#@dp.message_handler(commands=['Posizione'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Via Roma 163, Dello(Bs)")


#@dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['orario_di_lavoro'])
    dp.register_message_handler(pizza_place_command, commands=['Posizione'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])

