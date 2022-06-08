import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 Hai {message.from_user.mention()} !

        Saya adalah [{bn}](t.me/{bu}), bot yang bisa streaming di OS/VCG !

Semua perintah , kalian bisa cek perintah berikut : ( `/ . • $ ^ ~ + * ?` )
Jika kalian punya pertanyaan atau masalah lainnya kalian bisa PM [Owner](t.me/erojistrix)...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan saya ke grup anda", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "Developer", url=f"https://t.me/erojistrix"
                    ),
                    InlineKeyboardButton(
                        "Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "Inline", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Youtube", url="https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw"
                    )]
            ]
       ),
    )

