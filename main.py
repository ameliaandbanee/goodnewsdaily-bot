import asyncio
import os
from telegram import Bot

async def main():
    # 1. Try to get the token
    token = os.getenv("BOT_TOKEN")

    # 2. Advanced debugging prints for Railway logs
    print(f"DEBUG: BOT_TOKEN env variable exists in system: {'BOT_TOKEN' in os.environ}")
    print(f"DEBUG: Token value is None? {token is None}")
    if token:
        print(f"DEBUG: Token length: {len(token)} characters")
        # Strip any accidental hidden spaces or newlines just in case
        token = token.strip() 

    # 3. Initialize the bot
    if not token:
        raise ValueError("CRITICAL ERROR: BOT_TOKEN is completely empty or missing from Railway variables!")

    bot = Bot(token=token)
    me = await bot.get_me()
    print("Bot username:", me.username)

asyncio.run(main())
