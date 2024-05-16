# Derradji - SN 
import asyncio
from telegram import Bot
from telegram.error import TelegramError
from datetime import datetime


TOKEN = 'XXXXXX'
USER_ID = 'YYYYYY'

async def send_(bot, user_id=USER_ID):
    try:
        await bot.send_message(
                chat_id=user_id,
                text="null",
                caption=f"Time: {datetime.now().strftime('%D %H:%M')}"
            )
    except TelegramError as e:
        print("Error sending !", e)


async def send_data():
    bot = Bot(token=TOKEN)
    try:
        await send_(bot, USER_ID)
    except Exception as e:
        print("Error:", e)


# packages : asyncio, (in cv2 file : import TelegramBot) , python-telegram-bot==20.8
#  run : asyncio.run(TelegramBot.send_data())
