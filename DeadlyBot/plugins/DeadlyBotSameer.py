import os
import asyncio
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest

from Deadlybot.utils import deadly_cmd, edit_or_reply, sudo_cmd
DEFAULTUSER = Config.YOUR_NAME

DeadlyBot = bot.uid


bots = "@MissRose_bot"

BOTLOG_CHATID = Config.LOGGER_ID

G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)


@bot.on(deadly_cmd("superfban ?(.*)"))
@bot.on(sudo_cmd("superfban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"Starting superfban By [{DEFAULTUSER}](tg://user?id={DeadlyBot}) 😈")
    fedList = []
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message, "fedlist"
            )
            await asyncio.sleep(6)
            file = open(downloaded_file_name, "r")
            lines = file.readlines()
            for line in lines:
                try:
                    fedList.append(line[:36])
                except:
                    pass
            arg = event.text.split(" ", maxsplit=2)
            if len(arg) > 2:
                FBAN = arg[1]
                REASON = arg[2]
            else:
                FBAN = arg[1]
                REASON = " #MassBanned "
        else:
            FBAN = previous_message.sender_id
            REASON = event.text.split(" ", maxsplit=1)[1]
            if REASON.strip() == "":
                REASON = " #MassBanned "
    else:
        arg = event.text.split(" ", maxsplit=2)
        if len(arg) > 2:
            FBAN = arg[1]
            REASON = arg[2]
        else:
            FBAN = arg[1]
            REASON = " #MassBanned "
    try:
        int(FBAN)
        if int(FBAN) == 1559064347:
            await event.edit("Something Went wrong!")
            return
    except:
        if (
            FBAN == "@OFFICIAL_sameer" 
    
        ):
            await event.edit("Hey Nigga, You can't superfban your father😏")
            return
    if LOGGER_ID:
        chat = LOGGER_ID
    else:
        chat = await event.get_chat()
    if not len(fedList):
        for a in range(3):
            async with event.client.conversation("@MissRose_bot") as bot_conv:
                await bot_conv.send_message("/start")
                await bot_conv.send_message("/myfeds")
                await asyncio.sleep(3)
                response = await bot_conv.get_response()
                await asyncio.sleep(3)
                if "make a file" in response.text:
                    await asyncio.sleep(6)
                    await response.click(0)
                    await asyncio.sleep(6)
                    fedfile = await bot_conv.get_response()
                    await asyncio.sleep(3)
                    if fedfile.media:
                        downloaded_file_name = await event.client.download_media(
                            fedfile, "fedlist"
                        )
                        await asyncio.sleep(6)
                        file = open(downloaded_file_name, "r")
                        lines = file.readlines()
                        for line in lines:
                            try:
                                fedList.append(line[:36])
                            except:
                                pass
                    else:
                        return
                if len(fedList) == 0:
                    await event.edit(f"Something went wrong. Retrying ({a+1}/3)...")
                else:
                    break
        else:
            await event.edit(f"Error")
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True

            elif In:
                tempFedId += x
        if len(fedList) == 0:
            await event.edit("Something went wrong.")
            return
    await event.edit(f"Fbaning in {len(fedList)} feds by [{DEFAULTUSER}](tg://user?id={DeadlyBot}) 😈")
    try:
        await event.client.send_message(chat, f"/start")
    except:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(3)
    if EXCLUDE_FED:
        excludeFed = EXCLUDE_FED.split("|")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if EXCLUDE_FED and fed in excludeFed:
            await event.client.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await event.client.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await event.client.send_message(chat, f"/fban {FBAN} {REASON} \n\n#SUPERFBAN_BY_DEADLYBOT")
        await asyncio.sleep(3)
    await event.edit(f"SuperFBan Completed. Affected {len(fedList) - exCount} feds by [{DEFAULTUSER}](tg://user?id={DeadlyBot}) 😈")
