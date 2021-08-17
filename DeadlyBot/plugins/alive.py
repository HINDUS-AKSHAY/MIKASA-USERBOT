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

DEADLY_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
DEADLY_CAPTION = "🔥 ℓєgєη∂яу αƒ ∂єα∂ℓу кααℓ 🔥\n\n"
DEADLY_CAPTION += (
    f"                __↼🄼🄰🅂🅃🄴🅁⇀__\n  **『 {DEFAULTER} 』**\n\n"
)
DEADLY_CAPTION += f"╔══════════════════╗\n"
DEADLY_CAPTION += f"╠•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `{tel_ver}` \n"
DEADLY_CAPTION += f"╠•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{deadly_ver}`\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙶𝚁𝙾𝚄𝙿:`  [𝙹𝙾𝙸𝙽](t.me/DEADLY_KAAL_SUPPORT)\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [𝙹𝙾𝙸𝙽](t.me/deadly_kaal_bot)\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙲𝚁𝙴𝙰𝚃𝙾𝚁:` [⚡𝙿𝚁𝙾⚡](https://t.me/DEADLY_TECHY/83)\n"
DEADLY_CAPTION += f"╚══════════════════╝\n\n"
DEADLY_CAPTION += " [✨𝚁𝙴𝙿𝙾✨](https://github.com/DEADLY-FIGHTERS/DEADLY-KAAL-BOT) 🔹 [📜𝙻𝙸𝙲𝙴𝙽𝚂𝙴📜](https://github.com/DEADLY-FIGHTERS/DEADLY-KAAL-BOT/blob/main/LICENSE)"
                            
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


DEADLY_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
deadly_caption = f"**{Config.ALIVE_MSG}**\n\n"
deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"                
deadly_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
deadly_caption += f"┣•➳➠ `Tᴇʟᴇᴛʜᴏɴ:` `{tel_ver}` \n"
deadly_caption += f"┣•➳➠ `Vᴇʀsɪᴏɴ:` `{deadly_ver}`\n"
deadly_caption += f"┣•➳➠ `𝙰𝙱𝚄𝚂𝙴:` `{abuse_m}`\n"
deadly_caption += f"┣•➳➠ `Sᴜᴅᴏ:` `{is_sudo}`\n"
deadly_caption += f"┣•➳➠ `Cʜᴀɴɴᴇʟ:` [Jᴏɪɴ](Config.YOUR_CHANNEL)\n"
deadly_caption += f"┣•➳➠ `Gʀᴏᴜᴘ:` [Jᴏɪɴ](Config.YOUR_GROUP)\n"
deadly_caption += f"┗━━━━━━━━━━━━━━━━━━━\n" 


                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Awake", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
