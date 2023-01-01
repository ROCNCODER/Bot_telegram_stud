from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage=MemoryStorage()

TOK="5338219426:AAGWygEVie8iBPMYFqXkvG9yTgxC5oLfABo"
bot = Bot(token=TOK)
dp=Dispatcher(bot, storage=storage)
