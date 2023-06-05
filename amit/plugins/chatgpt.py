from telehon import events
import asyncio, openai
from .. import bot, openai_key

openai.api_key = openai_key

@bot.on(events.NewMessage(incoming = True,pattern = "(?i)/ask"))
async def _chatgpt(event):
  await event.reply(event)
