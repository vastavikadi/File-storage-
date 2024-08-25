from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import OWNER_ID
from helper_func import encode, get_message_id
import os, sys, time, asyncio, logging, datetime


is_restarting = False

@Client.on_message(filters.private & filters.user(OWNER_ID) & filters.command('restart'))
async def restart_bot(b, m):
    global is_restarting
    if not is_restarting:
        is_restarting = True
        await m.reply_text("<b>🔄 Restarting...</b>")

        # Gracefully stop the bot's event loop
        b.stop()
        time.sleep(2)  # Adjust the delay duration based on your bot's shutdown time

        # Restart the bot process
        os.execl(sys.executable, sys.executable, *sys.argv)