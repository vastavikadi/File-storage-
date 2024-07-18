from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=(
                "┏━━━━━━━━━━━━━━━━━┓\n"
                "ㅤㅤ   ㅤ  <a href='https://t.me/official_str'>sᴛᴇʀɴʀɪᴛᴛᴇʀ</a>ㅤㅤㅤㅤㅤ\n"
                "┗━━━━━━━━━━━━━━━━━┛\n\n"
                "╔──────\n"
                "╟ Owner: <a href='https://t.me/aryan_kadam'>Aryan Kadam</a>\n"
                "╚──────\n"
                "╔──────\n"
                "╟ <a href='https://t.me/animeplaza_str'>Anime Plaza STR</a>\n"
                "╚──────\n"
                "╔──────\n"
                "╟ <a href='https://t.me/ongoing_str'>Ongoing Anime</a>\n"
                "╚──────\n"
                "╔──────\n"
                "╟ Dev: <a href='https://t.me/corpsealone'>ɢӈߋʂτ</a>\n"
                "╚──────"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Join Anime Plaza", url='https://t.me/animeplaza_str')],
                    [InlineKeyboardButton("Join our group chat", url='https://t.me/OtakusMotel_STR')],
                    [InlineKeyboardButton("🔒 Close", callback_data="close")]
                ]
            ),
            parse_mode='HTML'  # Ensure 'parse_mode' is set to 'HTML'
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass