import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/10a5482207504a09bb448.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [𝐌𝐫 𝐊𝐚𝐧𝐧𝐚𝐝𝐢𝐠𝐚 🚩](https://t.me/mr_professor_agora)

𝐎𝐰𝐧𝐞𝐫 :-  [✨ 𝐌𝐫 𝐊𝐚𝐧𝐧𝐚𝐝𝐢𝐠𝐚 🚩 💛❤️](https://t.me/Mr_Professor_Agora)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [✨ 𝐊𝐚𝐧𝐧𝐚𝐝𝐢𝐠𝐚 𝐁𝐨𝐓𝐬 ❤️🎸](https://t.me/Kannadiga_BOTs)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [✨  𝐊𝐚𝐧𝐧𝐚𝐝𝐢𝐠𝐚 𝐓𝐞𝐫𝐫𝐢𝐭𝐨𝐫𝐲 🎧](https://t.me/Naan_1_Kannadiga)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [✨  𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗥𝗲𝗽𝗼 🌍](https://t.me/Naan_1_Kannadiga)
𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :- [✨𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗡𝗼𝘄 🚩](https://telegra.ph/𝙋𝙍𝙁𝙀𝙎𝙎𝙍-02-08-2)
𝐅𝐞𝐞𝐋𝐢𝐧𝐠'𝐒 :- [✨ 𝗝𝗼𝗶𝗻 ❤️🥀](https://t.me/ADM_DESIGNS)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝐌𝐫 𝐊𝐚𝐧𝐧𝐚𝐝𝐢𝐠𝐚 🚩 💛❤️](https://t.me/Mr_Kannadiga_Agora)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/Kannadiga_bots")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/10a5482207504a09bb448.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://t.me/Naan_1_Kannadiga")
                ]
            ]
        ),
    )
