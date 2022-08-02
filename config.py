#from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram
from decouple import config
storage = MemoryStorage()

TOKEN = config('TOKEN')
bot = aiogram.Bot(TOKEN)
dp = aiogram.Dispatcher(bot=bot, storage=storage)
ADMIN = [5453996037, ]
#URL = "https://python19botbot.herokuapp.com/"