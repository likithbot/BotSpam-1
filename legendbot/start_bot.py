from pyrogram import Client
from legendGirl.core import bot

async def start_bot():
    await bot.start()
    print("Bot started")
