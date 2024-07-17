import logging
import asyncio
from pyrogram import Client, filters
from telebot import TeleBot
from config import TG_BOT_TOKEN, API_ID, API_HASH, FORCE_SUB_CHANNEL, CHANNEL_ID

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the bot
bot = TeleBot(TG_BOT_TOKEN)

# Initialize the Pyrogram client
client = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TG_BOT_TOKEN)

# Define a simple start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot!")

# Define other command handlers
# Example: Handling the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "This is the help message.")

# Run the Pyrogram client
async def run():
    async with client:
        logger.info("Pyrogram client is running")
        await client.send_message("me", "Bot has started!")

        # Check the FORCE_SUB_CHANNEL and set the invite link
        if FORCE_SUB_CHANNEL:
            try:
                chat = await client.get_chat(FORCE_SUB_CHANNEL)
                logger.info(f"FORCE_SUB_CHANNEL found: {chat}")
                if not chat.invite_link:
                    await client.export_chat_invite_link(FORCE_SUB_CHANNEL)
                bot.invite_link = chat.invite_link
            except Exception as e:
                logger.warning(f"Error in FORCE_SUB_CHANNEL: {e}")

        # Check the DB Channel
        try:
            db_channel = await client.get_chat(CHANNEL_ID)
            logger.info(f"DB Channel found: {db_channel}")
            bot.db_channel = db_channel
            test = await client.send_message(chat_id=db_channel.id, text="Test Message")
            await client.delete_messages(chat_id=db_channel.id, message_ids=[test.message_id])
        except Exception as e:
            logger.warning(f"Error in CHANNEL_ID: {e}")

        me = await client.get_me()
        logger.info(f"Bot Running! @{me.username}")

        # Set bot commands
        bot.set_my_commands([
            {'command': 'start', 'description': 'Start the bot'},
            {'command': 'help', 'description': 'Help message'}
        ])

        # Start polling
        bot.polling(none_stop=True)

if __name__ == "__main__":
    asyncio.run(run())
