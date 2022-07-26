from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
#from keyboards import client_kb


#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Добро пожаловать на шоу {message.from_user.full_name}")


#@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"/start - Старт бота\n "
                           f"/mem - отправляет mem\n "
                           f"/menu - опрос гурмана\n "
                           f"/quiz - викторина\n "
                           f"/help - помошь в студию\n "
                           f"/game - игра ")


#@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    stick = open('media/1.png', 'rb')
    await bot.send_sticker(message.chat.id, sticker=stick)


#@dp.message_handler(commands=['quiz'])
async def quest_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Какой псевдоним у Marshall Marshall Bruce Mathers III?"
    answers = [
        'Snoop Dog', "50 CENT", "Jay-Z", "Eminem"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Ты не шаришь в музыке",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(quest_handler, commands=['quiz'])
