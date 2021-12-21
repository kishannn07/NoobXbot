import os

import yt_dlp
from NoobXbot import BOT_NAME, BOT_USERNAME, app
from NoobXbot.config import DURATION_LIMIT
from NoobXbot.NoobXUtilities.database.chats import is_served_chat
from NoobXbot.NoobXUtilities.helpers.filters import command
from NoobXbot.NoobXUtilities.helpers.gets import get_url
from NoobXbot.NoobXUtilities.helpers.inline import search_markup
from NoobXbot.NoobXUtilities.helpers.thumbnails import down_thumb
from NoobXbot.NoobXUtilities.helpers.ytdl import ytdl_opts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython import VideosSearch

flex = {}
chat_watcher_group = 3


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


@Client.on_message(
    command(["song", f"song@{BOT_USERNAME}", "vsong", f"vsong@{BOT_USERNAME}"])
)
async def mpthree(_, message: Message):
    chat_id = message.chat.id
    if message.sender_chat:
        return await message.reply_text(
            """
You are an Anonymous Admin!
Revert to User Account From Admin Rights.
"""
        )
    user_id = message.from_user.id
    message.chat.title
    message.from_user.first_name
    checking = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"

    url = get_url(message)
    if url:
        query = message.text.split(None, 1)[1]
        mystic = await message.reply_text("Processing")
        ydl_opts = {"format": "bestaudio/best"}
        try:
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"]
                (result["link"])
                (result["id"])
                videoid = result["id"]
        except Exception as e:
            return await mystic.edit_text(f"Soung Not Found.\n**Possible Reason:**{e}")
        smex = int(time_to_seconds(duration))
        if smex > DURATION_LIMIT:
            return await mystic.edit_text(
                f"**__Duration Error__**\n\n**Allowed Duration: **90 minute(s)\n**Received Duration:** {duration} minute(s)"
            )
        if duration == "None":
            return await mystic.edit_text("Sorry! Live videos are not Supported")
        if views == "None":
            return await mystic.edit_text("Sorry! Live videos are not Supported")
        thumb = await down_thumb(thumbnail, user_id)
        buttons = gets(videoid, user_id)
        m = await message.reply_text(
            f"""
<b>📌 Title:</b> [{title[:25]}]({url})
<b>💡</b> [More Information](https://t.me/{BOT_USERNAME}?start=info_{id})
<b>⚡ Supported</b> [{BOT_NAME}](t.me/{BOT_USERNAME})
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        os.remove(thumb)
    else:
        if len(message.command) < 2:
            await message.reply_text(
                """
**Try:**

/song or /vsong [Youtube Link] - song name manually
"""
            )
        query = message.text.split(None, 1)[1]
        mystic = await message.reply_text("**🔎 Searching**")
        try:
            a = VideosSearch(query, limit=5)
            result = (a.result()).get("result")
            title1 = result[0]["title"]
            duration1 = result[0]["duration"]
            title2 = result[1]["title"]
            duration2 = result[1]["duration"]
            title3 = result[2]["title"]
            duration3 = result[2]["duration"]
            title4 = result[3]["title"]
            duration4 = result[3]["duration"]
            title5 = result[4]["title"]
            duration5 = result[4]["duration"]
            ID1 = result[0]["id"]
            ID2 = result[1]["id"]
            ID3 = result[2]["id"]
            ID4 = result[3]["id"]
            ID5 = result[4]["id"]
        except Exception as e:
            return await mystic.edit_text(
                f"Song not found.\\in**Possible reasons:** {e}"
            )
        await mystic.delete()
        buttons = search_markup(
            ID1,
            ID2,
            ID3,
            ID4,
            ID5,
            duration1,
            duration2,
            duration3,
            duration4,
            duration5,
            user_id,
            query,
        )
        hmo = await message.reply_text(
            f"""
<b>📌 Please Select Song You Want To Download</b>


¹ <b>{title1[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID1})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

² <b>{title2[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID2})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

³ <b>{title3[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID3})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

⁴ <b>{title4[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID4})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

⁵ <b>{title5[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID5})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return


@Client.on_callback_query(filters.regex(pattern=r"beta"))
async def startyuplay(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    CallbackQuery.message.chat.id
    CallbackQuery.message.chat.title
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    try:
        id, duration, user_id = callback_request.split("|")
    except Exception as e:
        return await CallbackQuery.message.edit(
            f"Error Occured\n**Possible reason could be**:{e}"
        )
    if duration == "None":
        return await CallbackQuery.message.reply_text(
            f"Sorry!, Live Videos are not supported"
        )
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "This is not for you! Search You Own Song Nigga", show_alert=True
        )
    await CallbackQuery.message.delete()
    checking = f"[{CallbackQuery.from_user.first_name}](tg://user?id={userid})"
    url = f"https://www.youtube.com/watch?v={id}"
    videoid = id
    smex = int(time_to_seconds(duration))
    if smex > DURATION_LIMIT:
        await CallbackQuery.message.reply_text(
            f"**__Duration Error__**\n\n**Allowed Duration: **90 minute(s)\n**Received Duration:** {duration} minute(s)"
        )
        return
    try:
        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
            x = ytdl.extract_info(url, download=False)
    except Exception as e:
        return await CallbackQuery.message.reply_text(
            f"Failed to download this video.\n\n**Reason**:{e}"
        )
    title = x["title"]
    await CallbackQuery.answer(
        f"Selected {title[:20]}.... \nProcessing..", show_alert=True
    )
    thumbnail = x["thumbnail"]
    (x["id"])
    videoid = x["id"]
    thumb = await down_thumb(thumbnail, user_id)
    buttons = gets(videoid, user_id)
    m = await CallbackQuery.message.reply_photo(
        photo=thumb,
        reply_markup=InlineKeyboardMarkup(buttons),
        caption=f"""
<b>📌 Title:</b> [{title[:25]}]({url})
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{id})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})
""",
    )
    os.remove(thumb)
    await CallbackQuery.message.delete()


@Client.on_callback_query(filters.regex(pattern=r"chonga"))
async def chonga(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    print(callback_request)
    CallbackQuery.from_user.id
    try:
        id, query, user_id = callback_request.split("|")
    except Exception as e:
        return await CallbackQuery.message.edit(
            f"Error Occured\n**Possible reason could be**:{e}"
        )
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "This is not for you! Search You Own Song", show_alert=True
        )
    i = int(id)
    query = str(query)
    try:
        a = VideosSearch(query, limit=10)
        result = (a.result()).get("result")
        title1 = result[0]["title"]
        duration1 = result[0]["duration"]
        title2 = result[1]["title"]
        duration2 = result[1]["duration"]
        title3 = result[2]["title"]
        duration3 = result[2]["duration"]
        title4 = result[3]["title"]
        duration4 = result[3]["duration"]
        title5 = result[4]["title"]
        duration5 = result[4]["duration"]
        title6 = result[5]["title"]
        duration6 = result[5]["duration"]
        title7 = result[6]["title"]
        duration7 = result[6]["duration"]
        title8 = result[7]["title"]
        duration8 = result[7]["duration"]
        title9 = result[8]["title"]
        duration9 = result[8]["duration"]
        title10 = result[9]["title"]
        duration10 = result[9]["duration"]
        ID1 = result[0]["id"]
        ID2 = result[1]["id"]
        ID3 = result[2]["id"]
        ID4 = result[3]["id"]
        ID5 = result[4]["id"]
        ID6 = result[5]["id"]
        ID7 = result[6]["id"]
        ID8 = result[7]["id"]
        ID9 = result[8]["id"]
        ID10 = result[9]["id"]
    except Exception as e:
        return await mystic.edit_text(
            f"Song Not Found.\\in**Possible Reasons:** {e}"
        )
    if i == 1:
        buttons = search_markup2(
            ID6,
            ID7,
            ID8,
            ID9,
            ID10,
            duration6,
            duration7,
            duration8,
            duration9,
            duration10,
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"""
<b>📌 Please Select Song You Want To Download</b>


⁶ <b>{title6[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID6})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

⁷ <b>{title7[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID7})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

⁸ <b>{title8[:20]}</b>
├ 💡 [Get Additional Information](https://t.me/{BOT_USERNAME}?start=info_{ID8})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

⁹ <b>{title9[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID9})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

¹⁰ <b>{title10[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID10})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return
    if i == 2:
        buttons = search_markup(
            ID1,
            ID2,
            ID3,
            ID4,
            ID5,
            duration1,
            duration2,
            duration3,
            duration4,
            duration5,
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"""
<b>📌 Please Select Song You Want To Download</b>


¹ <b>{title1[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID1})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

² <b>{title2[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID2})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

³ <b>{title3[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID3})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

⁴ <b>{title4[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID4})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})

⁵ <b>{title5[:20]}</b>
├ 💡 [More Information](https://t.me/{BOT_USERNAME}?start=info_{ID5})
└ ⚡ **Supported:** [{BOT_NAME}](t.me/{BOT_USERNAME})
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="¹", callback_data=f"beta {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="²", callback_data=f"beta {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="³", callback_data=f"beta {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⁴", callback_data=f"beta {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="⁵", callback_data=f"beta {ID5}|{duration5}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👈", callback_data=f"chonga 1|{query}|{user_id}"
            ),
            InlineKeyboardButton(text="❌", callback_data=f"ppcl2 smex|{user_id}"),
            InlineKeyboardButton(
                text="👉", callback_data=f"chonga 1|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="⁶", callback_data=f"beta {ID6}|{duration6}|{user_id}"
            ),
            InlineKeyboardButton(
                text="⁷", callback_data=f"beta {ID7}|{duration7}|{user_id}"
            ),
            InlineKeyboardButton(
                text="⁸", callback_data=f"beta {ID8}|{duration8}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⁹", callback_data=f"beta {ID9}|{duration9}|{user_id}"
            ),
            InlineKeyboardButton(
                text="¹⁰", callback_data=f"beta {ID10}|{duration10}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👈", callback_data=f"chonga 2|{query}|{user_id}"
            ),
            InlineKeyboardButton(text="❌", callback_data=f"ppcl2 smex|{user_id}"),
            InlineKeyboardButton(
                text="👉", callback_data=f"chonga 2|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def gets(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 Audio", callback_data=f"gets audio|{videoid}|{user_id}"
            ),
            InlineKeyboardButton(
                text="Video 🎥", callback_data=f"gets video|{videoid}|{user_id}"
            ),
        ],
        [InlineKeyboardButton(text="🗑️ ClosE 🗑️", callback_data=f"close2")],
    ]
    return buttons
