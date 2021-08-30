from . import *

import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.messages import ImportChatInviteRequest


@bot.on(deadly_cmd(pattern="pjoin ?(.*)"))
@bot.on(sudo_cmd(pattern="pjoin ?(.*)", allow_sudo=True))
async def _(e):
        venom = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = venom[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )