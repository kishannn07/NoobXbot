import yt_dlp
from NoobXbot.config import SUPPORT_GROUP, UPDATES_CHANNEL
from NoobXbot import (
    ASSID,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    OWNER,
    SUDOERS,
    app,
)
from NoobXbot.NoobXUtilities.database.chats import is_served_chat
from NoobXbot.NoobXUtilities.database.queue import remove_active_chat
from NoobXbot.NoobXUtilities.database.sudo import get_sudoers
from NoobXbot.NoobXUtilities.helpers.inline import personal_markup
from NoobXbot.NoobXUtilities.helpers.thumbnails import down_thumb
from NoobXbot.NoobXUtilities.helpers.ytdl import ytdl_opts
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


def start_pannel():
    buttons = [
        [
            InlineKeyboardButton(text=f"My Home🔥", url=f"https://t.me/{SUPPORT_GROUP}"),
            InlineKeyboardButton(text=f"Channel🔥", url=f"https://t.me/{UPDATES_CHANNEL}"),
        ],
        [
            InlineKeyboardButton("🔥OWNER🔥", url=f"https://t.me/userderdead"),
            InlineKeyboardButton("🔥Commands", url=f"https://telegra.ph/Commands-12-20"),
        ],
    ]
    return (
        "🎛 **{BOT_NAME} I'm NoobXbot**",
        buttons,
    )


pstart_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➕ Take Me To Your Group​ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(text="📌 Support​", url=f"https://t.me/{SUPPORT_GROUP}"),
            InlineKeyboardButton("📌 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
        ],
        [
            InlineKeyboardButton("🔥 Commands", url=f"https://telegra.ph/Commands-12-20"),
        ],
    ]
)
welcome_captcha_group = 2


@app.on_message(filters.new_chat_members, group=welcome_captcha_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    for member in message.new_chat_members:
        try:
            if member.id in OWNER:
                return await message.reply_text(
                    f"💡 Owner Bot [{member.mention}] Boom boom owner."
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    f"💡 Admin Bot [{member.mention}] Boom boom sudo."
                )
            if member.id == ASSID:
                await remove_active_chat(chat_id)
            if member.id == BOT_ID:
                out = start_pannel()
                await message.reply_text(
                    f"""
👋 ** Thanks For Starting Me**

💡 **Take Me To Your Group**
""",
                    reply_markup=InlineKeyboardMarkup(out[1]),
                    disable_web_page_preview=True
                )
                return
        except BaseException:
            return


@Client.on_message(
    filters.group
    & filters.command(
        ["start", "help", f"start@{BOT_USERNAME}", f"help@{BOT_USERNAME}"]
    )
)
async def start(_, message: Message):
    chat_id = message.chat.id
    out = start_pannel()
    await message.reply_text(
        f"""
Here {message.chat.title}.
Thanks Of Using.

For assistance please click the button below.
""",
        reply_markup=InlineKeyboardMarkup(out[1]),
        disable_web_page_preview=True
    )
    return


@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def play(_, message: Message):
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        await app.send_message(
            message.chat.id,
            text=f"""
**✨ Welcome {rpk}!

💬 [{BOT_NAME}](t.me/{BOT_USERNAME}) Simple Music Player Bot Telegram!

💡 Helper Commands » 📚 https://telegra.ph/Commands-12-20 !**

""",
            parse_mode="markdown",
            reply_markup=pstart_markup,
            reply_to_message_id=message.message_id,
        )
    elif len(message.command) == 2:
        query = message.text.split(None, 1)[1]
        f1 = query[0]
        f2 = query[1]
        f3 = query[2]
        finxx = f"{f1}{f2}{f3}"
        if str(finxx) == "inf":
            query = (str(query)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                x = ytdl.extract_info(query, download=False)
            thumbnail = x["thumbnail"]
            searched_text = f"""
🔍 **Video Track Information**

❇️**Title:** {x["title"]}

⏳ **Duration:** {round(x["duration"] / 60)} Mins
👀 **Count:** `{x["view_count"]}`
👍 **Likes:** `{x["like_count"]}`
👎 **Dislikes:** `{x["dislike_count"]}`
⭐️ **Ratings:** {x["average_rating"]}
🎥 **Name channel:** {x["uploader"]}
📎 **Channel Link:** [Kunjungi Dari Sini]({x["channel_url"]})
🔗 **Link:** [Link]({x["webpage_url"]})
"""
            link = x["webpage_url"]
            buttons = personal_markup(link)
            userid = message.from_user.id
            thumb = await down_thumb(thumbnail, userid)
            await app.send_photo(
                message.chat.id,
                photo=thumb,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if str(finxx) == "sud":
            sudoers = await get_sudoers()
            text = "**📝 SUDO USER LIST**\n\n"
            for count, user_id in enumerate(sudoers, 1):
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name if not user.mention else user.mention
                except Exception:
                    continue
                text += f"- {user}\n"
            if not text:
                await message.reply_text("No Sudo User")
            else:
                await message.reply_text(text)
