from aiogram import types, Dispatcher
from config import bot, dp
import random


#@dp.message_handler()
async def echo(message: types.Message):
    try:
        i = int(message.text)
        await bot.send_message(message.from_user.id, i*i)
    except:
        await bot.send_message(message.from_user.id, message.text)

    if message.text.startswith('!pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.from_user.id != 'game':
        a = ('🏀', '⚽', '🎲', '🎯', '🎳', '🎰')
        await bot.send_dice(message.chat.id, emoji=random.choice(a))
        #bot_dice = a.dice.value


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)