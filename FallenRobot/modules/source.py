from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph//file/4cb8e92ea92564c66a421.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [𝙏𝙚𝙨𝙨𝙞𝙖 𝙀𝙧𝙖𝙡𝙞𝙩𝙝🇩](t.me/Tessia_Robot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝙓𝙚𝙡𝙘𝙞𝙪𝙨](tg://user?id=5132611794)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**𝙏𝙚𝙨𝙨𝙞𝙖 𝙀𝙧𝙖𝙡𝙞𝙩𝙝 sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=5132611794"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://t.me/TessiaXSupport")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
