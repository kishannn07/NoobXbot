import asyncio

from pyrogram import Client
from pytgcalls import idle

from NoobXbot import ASSNAME, BOT_NAME, app, client
from NoobXbot.config import API_HASH, API_ID, BOT_TOKEN, LOG_GROUP_ID
from NoobXbot.NoobXUtilities.database. import clean_restart_stage
from NoobXbot.NoobXUtilities.database.queue import get_active_chats, remove_active_chat
from NoobXbot.NoobXUtilities.noobxruns import run

Client(
    ":NoobXbot:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "NoobXbot.plugins"},
).start()


print(f"[INFO]: NOOBX BOT STARTED AS {BOT_NAME}!")
print(f"[INFO]: ASSISTANT STARTED AS {ASSNAME}!")


async def load_start():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[INFO]: SENDING RESTART STATUS")
        try:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted the Bot Successfully.**",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception:
        print("Error came while clearing db")
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)
        except Exception:
            print("Error came while clearing db")
    await app.send_message(LOG_GROUP_ID, "Bot Started")
    await client.send_message(LOG_GROUP_ID, "Assistant Started")
    await client.join_chat("noobXsupport")
    print("[INFO]: STARTED")


loop = asyncio.get_event_loop()
loop.run_until_complete(load_start())

run()
idle()
loop.close()

print("[LOG] CLOSING BOT")
