from . import *

@bot.on(deadly_cmd(pattern="spic"))
async def oho(event):
  if not event.is_reply:
    return await event.edit('Reply to a self distructing pic !.!.!')
  k = await event.get_reply_message()
  pic = await k.download_media()
  await bot.send_file(event.chat_id, pic, caption=f"""
  Oʜᴏ! LOL, Dᴇsᴛʀᴜᴄᴛɪᴏɴ Mᴏᴅᴇ Pɪᴄ Dᴇsᴛʀᴏʏᴇᴅ!\nPɪᴄ Dᴇsᴛʀᴏʏᴇᴅ Bʏ\n\n[✰ ᒪᗴᘜᗴᑎᗪᖇY ᗪᗴᗩᗪᒪY ᗷOT ✰](t.me/deadly_kaal_bot) 
  """)                                              
  await event.delete()
  
CmdHelp("Self Destruction").add_command(
  "spic", "This Command Can Capture The Self Destruction Picturr"
).add_info(
  "Capture 🤫 Pic."
).add_warning(
  "✅ Harmless Module."
).add()
