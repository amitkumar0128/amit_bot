from telethon import TelegramClient
import logging
import time

openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "5794992821:AAEKme5J8AIXTgy-gkDSwbScn5yWLLu1PsI"

bot = TelegramClient("amitbota", api_id, api_hash).start(bot_token = bot_token)