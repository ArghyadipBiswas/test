import os
from subprocess import run as shell
from pyrogram import *

bot = Client(
  "my project",
  api_id=6235351,
  api_hash="f68fde1378da8f85a243f2ae57f2fcf9",
  bot_token="5378163079:AAHhtCs9RPaEmux-UAiQOo7KVDmFRwMnd4o"
)
message = Client.get_messages(5042525177, "/mirror *")
link = message.replace('/mirror ', '')

async def main():
    async with app:
        await app.send_message("5042525177", link)
