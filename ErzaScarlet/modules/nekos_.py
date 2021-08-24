import nekos, os, random

from pyrogram import Client, filters
from pyrogram.types import Message

from ErzaScarlet import pbot
from ErzaScarlet.utils.ut import get_arg

neko_category = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']

@pbot.on_message(filters.command("nekos"))
async def hmm(client, message):
    owo = message.text[7:]
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    if owo in neko_category:
        hell = await message.reply(f"`Searching {owo} ...`")
        link = nekos.img(owo)
        try:
            if link.endswith(".gif"):
               await client.send_animation(chat_id=message.chat.id, animation=link, reply_to_message_id=reply_id)
               await hell.delete()
            else:
                await client.send_photo(chat_id=message.chat.id, photo=link, reply_to_message_id=reply_id)
        except Exception as e:
            await hell.edit(f"**ERROR !!**\n\n`{e}`")
    elif owo == "":
        hell = await message.reply("`Searching randoms...`")
        uwu = random.choice(neko_category)
        link = nekos.img(uwu)
        try:
            if link.endswith(".gif"):
               await client.send_animation(chat_id=message.chat.id, animation=link, reply_to_message_id=reply_id)
               await hell.delete()
            else:
                await client.send_photo(chat_id=message.chat.id, photo=link, reply_to_message_id=reply_id)
        except Exception as e:
            await hell.edit(f"**ERROR !!**\n\n`{e}`")
    else:
        await message.reply("**Unmatched argument.** \n\n__Get all the required queries for nekos here__ -> **[Nekos Queries](http://telegra.ph/Nekos-Queries-08-20)**")


        