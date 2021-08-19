import asyncio
import os
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon import functions, types, events
from . import *

logs_id = Config.FBAN_LOG_GROUP
fbot = "@MissRose_bot"


@bot.on(deadly_cmd(pattern="newfed ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="newfed ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    deadly_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    await eor(event, "`Making new fed...`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=609517172)
            )
            await event.client.send_message(chat, f"/newfed {deadly_input}")
            response = await response
        except YouBlockedUserError:
            await eod(event, "`Please unblock` @MissRose_Bot `and try again`")
            return
        if response.text.startswith("You already have a federation"):
            await eod(event,
                "You already have a federation. Do .renamefed to rename your current fed."
            )
        else:
            await eod(event, f"{response.message.message}", 7)


@bot.on(deadly_cmd(pattern="renamefed ?(.*)"))
@bot.on(sudo_cmd(pattern="renamefed ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    deadly_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    await event.edit("`Trying to rename your fed...`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=609517172))
              await event.client.send_message(chat, f"/renamefed {deadly_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @MissRose_Bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


@bot.on(deadly_cmd(pattern="fstat ?(.*)"))
@bot.on(sudo_cmd(pattern="fstat ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    deadly = await eor(event, "`Collecting fstat....`")
    thumb = deadly_logo
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        lavde = str(previous_message.sender_id)
        user = f"[user](tg://user?id={lavde})"
    else:
        lavde = event.pattern_match.group(1)
        user = lavde
    if lavde == "":
        await deadly.edit(
            "`Need username/id to check fstat`"
        )
        return
    else:
        async with bot.conversation(fbot) as conv:
            try:
                await conv.send_message("/fedstat " + lavde)
                await asyncio.sleep(4)
                response = await conv.get_response()
                await asyncio.sleep(2)
                await bot.send_message(event.chat_id, response)
                await event.delete()
            except YouBlockedUserError:
                await deadly.edit("`Please Unblock` @MissRose_Bot")


@bot.on(deadly_cmd(pattern="fedinfo ?(.*)"))
@bot.on(sudo_cmd(pattern="fedinfo ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    deadly = await eor(event, "`Fetching fed info.... please wait`")
    lavde = event.pattern_match.group(1)
    async with bot.conversation(fbot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + lavde)
            massive = await conv.get_response()
            await deadly.edit(massive.text + "\n\n**ʟɛɢɛռɖaʀʏ_ᴀғ_ɦɛʟʟɮօt**")
        except YouBlockedUserError:
            await deadly.edit("`Please Unblock` @MissRose_Bot")


# op superfban by sameer op

import os
import asyncio
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest

from DeadlyBot.utils import deadly_cmd, edit_or_reply, sudo_cmd
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
        await event.client.send_message(chat, f"/fban {FBAN} {REASON} \n\n#SUPERFBAN_BY_DeadlyBot")
        await asyncio.sleep(3)
    await event.edit(f"SuperFBan Completed. Affected {len(fedList) - exCount} feds by [{DEFAULTUSER}](tg://user?id={DeadlyBot}) 😈")

         
            
CmdHelp("federation").add_command(
  "newfed", "<newfed name>", "Makes a federation of Rose bot"
).add_command(
  "renamefed", "<new name>", "Renames the fed of Rose Bot"
).add_command(
  "fstat", "<username/id>", "Gets the fban stats of the user from rose bot federation"
).add_command(
  "fedinfo", "<fed id>", "Gives details of the given fed id"
).add_info(
  "Rose Bot Federation."
).add_warning(
  "✅ Harmless Module."
).add()
