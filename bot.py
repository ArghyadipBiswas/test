import os
from subprocess import run as shell
from pyrogram import *

bot = Client(
  "my project",
  api_id=6235351,
  api_hash="f68fde1378da8f85a243f2ae57f2fcf9",
  bot_token="5378163079:AAHhtCs9RPaEmux-UAiQOo7KVDmFRwMnd4o"
)
@bot.on_message(filters.command('start'))
def command1(bot, message):
    message.reply_text("i am alive.")

@bot.on_message(filters.command('mirror'))
def command2(bot, message):
    message.reply_text(message.text[7:])


bot.run()
