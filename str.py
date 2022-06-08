

import asyncio

from pyrogram import Client


print("𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙰𝙿𝙿 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙵𝚁𝙾𝙼 my.telegram.org/apps below.")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
