# credit goes to @D3_krish and @official_sameer

from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *


#-------------------------------------------------------------------------------
DEFAULTER = Config.YOUR_NAME

@bot.on(deadly_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(deadly):
    if deadly.fwd_from:
        return
    await deadly.get_chat()
    await deadly.delete()
    await bot.send_file(deadly.chat_id, DEADLY_PIC, caption=DEADLY_CAPTION)
    await deadly.delete()

DEADLY_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/75abec1279eafadb7f4dd.jpg"
DEADLY_CAPTION = "π₯ βΡgΡΞ·βΡΡ Ξ±Ζ βΡΞ±ββΡ βΞ±Ξ·Ξ±Ξ½ π₯\n\n"
DEADLY_CAPTION += (
    f"                __βΌπΌπ°πππ΄πβ__\n  **γ {deadly_mention} γ**\n\n"
)
DEADLY_CAPTION += f"βββββββββββββββββ\n"
DEADLY_CAPTION += f"β β’β³β  `ππ΄π»π΄ππ·πΎπ½:` `{tel_ver}` \n"
DEADLY_CAPTION += f"β β’β³β  `ππ΄πππΈπΎπ½:` `{deadly_ver}`\n"
DEADLY_CAPTION += f"β β’β³β  `πΆππΎππΏ:`  [πΉπΎπΈπ½](t.me/DEADLY_DANAV_SUPPORT)\n"
DEADLY_CAPTION += f"β β’β³β  `π²π·π°π½π½π΄π»:` [πΉπΎπΈπ½](t.me/deadly_DANAV_bot)\n"
DEADLY_CAPTION += f"β β’β³β  `π²ππ΄π°ππΎπ:` [β‘πΏππΎβ‘](t.me/DEADLY_SAMEER)\n"
DEADLY_CAPTION += f"βββββββββββββββββ\n\n"
DEADLY_CAPTION += " [β¨π³π΄πΏπ»πΎπ ππΎππ πΎππ½ π±πΎπβ¨](https://github.com/DEADLY-FIGHTERS/DEADLY-DANAV-BOT)"
                                            
#_______



@bot.on(deadly_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def up(deadly):
    if deadly.fwd_from:
        return
    await deadly.get_chat()
    await deadly.delete()
    await bot.send_file(deadly.chat_id, DEADLY_PIC, caption=deadly_caption)
    await deadly.delete()

deadly_caption = f"π₯ βΡgΡΞ·βΡΡ Ξ±Ζ βΡΞ±ββΡ βΞ±Ξ·Ξ±Ξ½ π₯\n\n"
deadly_caption += f"ββββββββββββββββββββββββββββ\n\n"
deadly_caption += f"**{Config.ALIVE_MSG}**\n\n"
deadly_caption += f"ββββββββββββββββββββββββββββ\n\n"                
deadly_caption += f"π£ π°π±πΎππ πΌπ πππππ΄πΌ π£\n\n"
deadly_caption += f"βΎ `ππ΄π»π΄ππ·πΎπ½` β£ `{tel_ver}` \n"
deadly_caption += f"βΎ `πππ³πΎ πΌπΎπ³π΄:` β£ `{is_sudo}`\n"
deadly_caption += f"βΎ πΌπ π²π·π°π½π½π΄π»: β£ [πΉπΎπΈπ½](t.me/Config.YOUR_CHANNEL)\n"
deadly_caption += f"βΎ πΌπ πΆππΎππΏ: β£ [πΉπΎπΈπ½](t.me/Config.YOUR_GROUP)\n\n"
deadly_caption += f"[β¨ π³π΄πΏπ»πΎπ ππΎππ π³π΄π°π³π»π π³π°π½π°π β¨](https://github.com/DEADLY-FIGHTERS/DEADLY-DANAV-BOT)\n" 
                                     
                                 
                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Awake", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "β Harmless Module"
).add()
