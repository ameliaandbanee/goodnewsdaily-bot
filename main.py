import asyncio
import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@GoodnewsdailySriLanka"

async def main():
    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text="🙏 Test message from Good News Daily Bot\n\nRailway + GitHub + Telegram are connected successfully."
    )

    print("Message sent successfully!")

asyncio.run(main())
