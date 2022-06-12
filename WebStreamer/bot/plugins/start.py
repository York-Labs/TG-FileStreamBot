# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]
# Translate : York Zhao [@York618]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'泥吼呀 {m.from_user.mention(style="md")}, 向我丢一个文件，然后得到属于你的直链吧！'
    )
