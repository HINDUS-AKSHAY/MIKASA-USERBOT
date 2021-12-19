import random
import re
import time

import requests
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from . import *


@bot.on(admin_cmd(pattern=f"repo", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo", allow_sudo=True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "[𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴](https://github.com/DEADLY-FIGHTERS/DeadlY-DANAV-BOT) 𝚃𝙾 𝙾𝙿𝙴𝙽 𝚃𝙷𝙸𝚂 \n🔥**𝙻𝙸𝚃 𝙰𝙵!!**🔥 𝙳𝙴𝙰𝙳𝙻𝚈 𝙳𝙰𝙽𝙰𝚅 𝙱𝙾𝚃.\n\n[👑 𝙳𝙴𝙰𝙳𝙻𝚈 𝙵𝙸𝙶𝙷𝚃𝙴𝚁𝚂 👑](t.ME/DEADLY_FIGHTERS)")

