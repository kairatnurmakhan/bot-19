from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot



#@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quest_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Сколько часов в сутках?"
    answers = [
        '23',
        '12',
        '24',
        '1',
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Даже люди Древнего Майя знают этот ответ",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )



#@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quest_2(call: types.CallbackQuery):
    question = "Сколько месяцев в високосном году?"
    answers = [
        '11',
        '12',
        '13',
        '11.5',
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Даже люди Древнего Майя знают этот ответ",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quest_1, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quest_2, lambda call: call.data == "button_call_2")