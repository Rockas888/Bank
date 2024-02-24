from pyrogram import filters
from pyrogram import Client as stark
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import os
import sys


@stark.on_message(filters.command(["start"]) & ~filters.edited)
async def Start_msg(bot: stark , m: Message):
    await bot.send_photo(
    m.chat.id,
    photo="https://telegra.ph/file/cef3ef6ee69126c23bfe3.jpg",
    caption = "**Hi i am All in One Extractor Bot**.\n"
                            "Press **menu commands** to**to use bot**..\n\n"
                            "**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : Invisible 😁**")
           


@stark.on_message(filters.command(["restart"]) & ~filters.edited)
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@stark.on_message(filters.command(["log"]) & ~filters.edited)
async def log_msg(bot: stark , m: Message):   
    await bot.send_document(m.chat.id, "log.txt")
