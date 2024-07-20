from aiohttp import web
from plugins import web_server
import logging
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
from datetime import datetime
import sys
from config import API_HASH, API_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT, FORCE_SUB_CHANNEL2

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
        self.invitelink1 = None
        self.invitelink2 = None

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        await self.export_invite_links()
        
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/paradoxdump")
        self.LOGGER(__name__).info(f""" \n\n       
 [PARADOX]
                                          """)
        self.username = usr_bot_me.username

        # web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    async def export_invite_links(self):
        await self.export_invite_link(FORCE_SUB_CHANNEL, 'invitelink1')
        await self.export_invite_link(FORCE_SUB_CHANNEL2, 'invitelink2')

    async def export_invite_link(self, channel_id, link_attr):
        if channel_id:
            try:
                chat = await self.get_chat(channel_id)
                link = chat.invite_link
                if not link:
                    link = await self.export_chat_invite_link(channel_id)
                setattr(self, link_attr, link)
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(f"Bot can't Export Invite link from Force Sub Channel {channel_id}!")
                self.LOGGER(__name__).warning(f"Please double-check the {link_attr} value and make sure the bot is an admin in the channel with Invite Users via Link Permission. Current Force Sub Channel Value: {channel_id}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/paradoxdump for support")
                sys.exit()

# Initialize the bot
bot = Bot()

# Ensure the bot starts and sets the invite links
bot.run()