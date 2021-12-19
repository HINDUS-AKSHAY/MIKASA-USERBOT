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

DEADLY_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/37ac22fe95355d62c2d76.mp4"
DEADLY_CAPTION = "🔥 ℓєgєη∂яу αƒ ∂єα∂ℓу ∂αηαν 🔥\n\n"
DEADLY_CAPTION += (
    f"                __↼𝙼𝙰𝚂𝚃𝙴𝚁⇀__\n  **『 {deadly_mention} 』**\n\n"
)
DEADLY_CAPTION += f"╔═══════════════╗\n"
DEADLY_CAPTION += f"╠•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `{tel_ver}` \n"
DEADLY_CAPTION += f"╠•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{deadly_ver}`\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙶𝚁𝙾𝚄𝙿:`  [𝙹𝙾𝙸𝙽](t.me/DEADLY_DANAV_SUPPORT)\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [𝙹𝙾𝙸𝙽](t.me/deadly_DANAV_bot)\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙲𝚁𝙴𝙰𝚃𝙾𝚁:` [⚡𝙿𝚁𝙾⚡](t.me/DEADLY_SAMEER)\n"
DEADLY_CAPTION += f"╚═══════════════╝\n\n"
DEADLY_CAPTION += " [✨𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙾𝚃✨](https://github.com/DEADLY-FIGHTERS/DEADLY-DANAV-BOT)"
                                            
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

deadly_caption = f"🔥 ℓєgєη∂яу αƒ ∂єα∂ℓу ∂αηαν 🔥\n\n"
deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"
deadly_caption += f"**{Config.ALIVE_MSG}**\n\n"
deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"                
deadly_caption += f"𖣘 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈 𝚂𝚈𝚂𝚃𝙴𝙼 𖣘\n\n"
deadly_caption += f"➾ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽` ➣ `{tel_ver}` \n"
deadly_caption += f"➾ `𝚂𝚄𝙳𝙾 𝙼𝙾𝙳𝙴:` ➣ `{is_sudo}`\n"
deadly_caption += f"➾ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_CHANNEL)\n"
deadly_caption += f"➾ 𝙼𝚈 𝙶𝚁𝙾𝚄𝙿: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_GROUP)\n\n"
deadly_caption += f"[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙳𝙴𝙰𝙳𝙻𝚈 𝙳𝙰𝙽𝙰𝚅 ✨](https://github.com/DEADLY-FIGHTERS/DEADLY-DANAV-BOT)\n" 
                                     
                                 
                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Awake", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
