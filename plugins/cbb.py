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
                "╟ Network: <a href='https://t.me/STERN_LEGION'>THE STERN LEGION</a>\n"
                "┗━━━━━━━━━━━━━━━━━┛\n\n"
                "╔──────\n"
                "╟ Network Owner: <a href='https://t.me/Aryan_Kadam'>Aryan ζ</a>\n"
                "╚──────\n"
                "╔──────\n"
                "╟ Anime Channel: <a href='https://t.me/AnimePlaza_STR'>Anime Plaza ||「𝚂𝚃𝚁」</a>\n"
                "╚──────\n"
                "╔──────\n"
                "╟ Movies & Series Channel: <a href='https://t.me/CinemaStack_Official'>Cinema Stack</a>\n"
                "╚──────\n"
                "╔──────\n"
                "╟ Devs: <a href='https://t.me/corpsealone'>ɢʜᴏsᴛ</a>\n<a href='https://t.me/JustMe_Charz'>𝙲𝚑𝚊𝚛𝚣🍷</a>\n<a href='vastavikportfolio.vercel.app'>VastavikAdi</a>\n"
                "╚──────"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Join THE STERN LEGION", url='https://t.me/STERN_LEGION')],
                    [InlineKeyboardButton("Join Anime Plaza ||「𝚂𝚃𝚁」", url='https://t.me/AnimePlaza_STR')],
                    [InlineKeyboardButton("Join Cinema Stack", url='https://t.me/CinemaStack_Official')],
                    [InlineKeyboardButton("Join Otakus' Motel ||「𝚂𝚃𝚁」", url='https://t.me/OtakusMotel_STR')],
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
