
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>ɢӈߋʂτ</a>\n\n○ Source Code : <a href='https://t.me/ghost_kun'>Click here</a>\n○ <a href='https://t.me/corpsealone'>[ᴘᴀʀᴀᴅᴏx]</a>\n○ Support Group : @paradoxdump</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Join Sternritter", url='https://t.me/sternriyal')],
                    [InlineKeyboardButton("🔒 Close", callback_data="close")]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass