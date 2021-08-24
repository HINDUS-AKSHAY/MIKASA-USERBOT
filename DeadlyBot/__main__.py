import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from DeadlyBot import LOGS, bot, tbot
from DeadlyBot.config import Config
from DeadlyBot.utils import load_module
from DeadlyBot.version import __deadly__ as deadlyver
hl = Config.HANDLER
DEADLY_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"

# let's get the bot ready
async def deadly_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"DEADLY_KAAL_SESSION - {str(e)}")
        sys.exit()


# DeadlyBot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 DEADLY BOT KO START KR RHE HAI DADA 🔰")
            bot.loop.run_until_complete(deadly_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 DEADLY KAAL BOT STARTUP COMPLETE 🔥 AB BASS PLUGINS DAALNA HE WAIT KRO 😂😂🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "DeadlyBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/The-DeadlyBot/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "DeadlyBot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ YOUR BOT IS NOW READY BABE ⚡")
LOGS.info(
    "CONGRATULATIONS 🥳🥳🎊🎊 YOUR DEADLY KAAL BOT IS DEPLOYED 🎊 ... NOW TYPE .ping OR .alive TO CHECK OUR AMAZING BOT 🥳🔥 IF U HAVE ANY PROBLEM THEN JOIN @DEADLY_KAAL_BOT"
)

# that's life...
async def deadly_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                DEADLY_PIC,
                caption=f"#START \n\nDeployed ∂єα∂ℓу кααℓ Bσт Successfully\n\n**∂єα∂ℓу кααℓ Bσт - {deadlyver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [∂єα∂ℓу кααℓ Bσт Channel](t.me/deadly_kaal_bot) for Updates & [∂єα∂ℓу кααℓ Bσт Chat](t.me/deadly_kaal_support) for any query regarding ∂єα∂ℓу кααℓ Bσт",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join DeadlyBot Channel after deploying 🤐😅
    try:
         await bot(JoinChannelRequest("@deadly_kaal_bot"))
         await bot(JoinChannelRequest("@deadly_kaAL_SUPPORT"))
         await bot(JoinChannelRequest("@deadly_FIGHTERS"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@deadly_userbot"))
#    except BaseException:
#        pass


bot.loop.create_task(deadly_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# DeadlyBot
