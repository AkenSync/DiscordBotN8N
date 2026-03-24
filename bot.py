import discord
import requests
import os

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id != CHANNEL_ID:
        return
    requests.post(N8N_WEBHOOK_URL, json={
        "content": message.content,
        "author": message.author.name,
        "channel_id": str(message.channel.id)
    })

client.run(os.getenv("DISCORD_TOKEN"))
