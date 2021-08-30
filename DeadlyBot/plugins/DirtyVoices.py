# credits - shinchan hell

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


@borg.on(deadly_cmd(pattern="dvoice?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "💁Zaps📢{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


            
CmdHelp("adult").add_command(
  "dvoice", None, "use and see For 18+ only kids don't use"
).add_warning(
  "For 18+ only kids don't use"
).add()
