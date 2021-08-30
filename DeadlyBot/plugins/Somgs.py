# credits - shinchan

from . import *


@bot.on(deadly_cmd(pattern="song ?(.*)"))
@bot.on(sudo_cmd(pattern="song ?(.*)", allow_sudo=True))
async def _(event):
    deadly_ = event.text[4:]
    if deadly_ == "":
        return await eor(event, "Give a song name to search")
    deadly = await eor(event, f"Searching song `{deadly_}`")
    somg = await event.client.inline_query("Lybot", f"{(deEmojify(deadly_))}")
    if somg:
        fak = await somg[0].click(Config.LOGGER_ID)
        if fak:
            await bot.send_file(
                event.chat_id,
                file=fak,
                caption=f"**Song by :** {deadly_mention}",
            )
        await deadly.delete()
        await fak.delete()
    else:
        await deadly.edit("**ERROR 404 :** __NOT FOUND__")


CmdHelp("somgs").add_command(
    "so", "<song name>", "Search the given song and uploads to current chat.", "so into your arms"
).add_info(
    "Fastest Song Module."
).add_warning(
    "✅ Harmless Module."
).add()
