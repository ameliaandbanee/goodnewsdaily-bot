import asyncio
import os
from telegram import Bot

async def main():
    token = os.getenv("BOT_TOKEN")

    print("Token found:", token is not None)

    bot = Bot(token=token)

    me = await bot.get_me()

    print("Bot username:", me.username)

asyncio.run(main())
