from bot import Bot
import time
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from helper_func import get_readable_time

# MongoDB URI
DB_URI = "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoDB client
mongo_client = AsyncIOMotorClient(DB_URI)
db = mongo_client['your_database_name']  # Replace with your database name

# Function to calculate ping
async def get_ping(bot: Bot) -> float:
    start = time.time()
    await bot.get_me()  # Simple call to measure round-trip time
    end = time.time()
    return round((end - start) * 1000, 2)  # Ping in milliseconds

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    uptime = get_readable_time(delta.seconds)

    # Get ping
    ping = await get_ping(bot)

    # Get DB response time
    db_response_time = await get_db_response_time()

    # Format the stats message
    stats_text = (
        f"Bot Uptime: {uptime}\n"
        f"Ping: {ping} ms\n"
        f"Database Response Time: {db_response_time} ms\n"
    )

    await message.reply(stats_text)

# Function to measure DB response time
async def get_db_response_time() -> float:
    start = time.time()
    # Perform a simple query
    await db.command("ping")
    end = time.time()
    return round((end - start) * 1000, 2)  # DB response time in milliseconds