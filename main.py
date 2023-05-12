from typing import Any
import discord
import bot
from discord.flags import Intents

token = 'hi'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    #coroutine waits for messages!
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(token)