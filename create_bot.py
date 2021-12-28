from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "5023040784:AAHQEGDyaZW5Ho-zBOPEQrGe_UhlrleMeQo"

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
