import asyncio
from pyrogram import Client
from helpers.filters import command
from config import SUDO_USERS, BOT_NAME as bn, BOT_USERNAME as lel, PMPERMIT, OWNER_USERNAME
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                f"Hai {message.from_user.mention()},\n\nSaya adalah akun asiten dari [{bn}](t.me/{lel}).\n\nJangan mencoba spam di PESAN PRIBADI ! supaya tidak terblok !\n\nJika terblok Hubungi[Azuman](t.me/erojistrix).",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤖 Bot", url=f"https://t.me/{lel}"
                    ),
                    InlineKeyboardButton(
                        "📥 Support", url="https://t.me/AzumanProjects"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "👤 Developer", url=f"https://t.me/erojistrix"
                    )]
            ]
        ),

    )
            return


@Client.on_message(filters.command(["pm", "pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("**✅ PM-PERMIT diaktifkan...**")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("**❎ PM-PERMIT dinonaktifkan...**")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**✅ Disetujui pesan pribadi oleh admin ...**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", ["!", ".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**✅ Disetujui untuk PM...**")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", ["!", ".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("**❎ Ditolak untuk PM...**")
        return
    message.continue_propagation()
