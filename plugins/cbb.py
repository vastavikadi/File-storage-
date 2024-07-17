
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"        "┏━━━━━━━━━━━━━━━━━┓\n"
        "ㅤㅤ   ㅤ  <a href='https://t.me/official_str'>sᴛᴇʀɴʀɪᴛᴛᴇʀ</a>ㅤㅤㅤㅤㅤ\n"
        "┗━━━━━━━━━━━━━━━━━┛\n\n"
        "╔──────\n"
        "╟ Owner: <a href='https://t.me/aryan_kadam>Aryan Kadam</a>\n"
        "╚──────\n"
        "╔──────\n"
        "╟ <a href='https://t.me/animeplaza_str'>Anime Plaza STR</a>\n"
        "╚──────\n"
        "╔──────\n"
        "╟ <a href='https://t.me/ongoing_str'>Ongoing Anime</a>\n"
        "╚──────\n"
        "╔──────\n"
        f"╟ Dev: <a href='https://t.me/corpsealone>ɢӈߋʂτ</a>\n"
        "╚──────",
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