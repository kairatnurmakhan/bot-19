import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="OK")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Пора спать!")


async def wake_up():
    video = open("media/video.mp4", "rb")
    await bot.send_video(chat_id=chat_id, video=video, caption="ПРОСНИСЬ И ПОЙ!")


async def scheduler():
    aioschedule.every().monday.at("22:00").do(go_to_sleep)
    aioschedule.every().monday.at("07:00").do(wake_up)

    aioschedule.every().tuesday.at("22:00").do(go_to_sleep)
    aioschedule.every().tuesday.at("07:00").do(wake_up)

    aioschedule.every().wednesday.at("22:00").do(go_to_sleep)
    aioschedule.every().wednesday.at("07:00").do(wake_up)

    aioschedule.every().thursday.at("22:00").do(go_to_sleep)
    aioschedule.every().thursday.at("07:00").do(wake_up)

    aioschedule.every().friday.at("22:00").do(go_to_sleep)
    aioschedule.every().friday.at("07:00").do(wake_up)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)