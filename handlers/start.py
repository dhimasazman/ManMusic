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
        caption=f""" Hai {message.from_user.mention()} 👋

Saya adalah [{bn}](t.me/{bu}), bot yang bisa streaming musik di OS/VCG !
jangan sungkan tambahkan saya ke grup anda ya...

Semua perintah , kalian bisa pakai simbol berikut : ( `/ . • $ ^ ~ + * ?` )

Jika kalian punya pertanyaan atau masalah lainnya kalian bisa hubungi [Owner](t.me/erojistrix)

**Jika kalian ingi donasi supaya projek ini terus berkembang kalian boleh donasi [Disini](https://bit.ly/donasidhimasazman)**

[Channel](t.me/AzumanProjects) • [Grup](t.me/AzumanSquad) • [Repo](https://github.com/dhimasazman/ManMusic)""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "➕ Tambahkan saya ke grup anda ➕", url=f"https://t.me/{bu}?startgroup=true"
                    ),
                ],[
                    InlineKeyboardButton(
                        "👤 Developer", url=f"https://t.me/erojistrix"
                    ),
                    InlineKeyboardButton(
                        "📥 Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "Inline", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "📺 Youtube", url="https://youtube.com/channel/dhimasazman"
                    )
                ],[
                    InlineKeyboardButton(
                        "📝 Repo", url=f"https://github.com/dhimasazman/ManMusic"
                    ),
                ]
            ]
       ),
    )

