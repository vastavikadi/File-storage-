from aiohttp import web
from plugins import web_server
import logging
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
from datetime import datetime
import sys
from config import API_HASH, API_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT
from pymongo import MongoClient
from config import DB_URI as MONGO_URI

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.web_app_runner = None  # For managing the web server
        self.mongo_client = None  # MongoDB client

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Initialize MongoDB client
        self.mongo_client = MongoClient(MONGO_URI)
        try:
            # Test MongoDB connection
            self.mongo_client.admin.command('ping')
            self.LOGGER(__name__).info("MongoDB connection established.")
        except Exception as e:
            self.LOGGER(__name__).error(f"Failed to connect to MongoDB: {e}")
            sys.exit(1)

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make sure the bot is Admin in the DB Channel, and double-check the CHANNEL_ID value, current value: {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped")
            sys.exit(1)

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/paradoxdump")
        self.LOGGER(__name__).info(f""" \n\n       
 [PARADOX]
                                          """)
        self.username = usr_bot_me.username

        # Start the web server
        self.web_app_runner = web.AppRunner(await web_server())
        await self.web_app_runner.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(self.web_app_runner, bind_address, PORT).start()

    async def stop(self, *args):
        # Stop the web server
        if self.web_app_runner:
            await self.web_app_runner.cleanup()

        # Close MongoDB client
        if self.mongo_client:
            self.mongo_client.close()
            self.LOGGER(__name__).info("MongoDB connection closed.")

        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

# Initialize the bot
bot = Bot()

# Ensure the bot starts and stops properly
try:
    bot.run()
except (KeyboardInterrupt, SystemExit):
    logging.info("Bot interrupted or system exit detected.")
finally:
    bot.stop()
    logging.info("Shutdown complete.")
