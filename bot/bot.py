import discord
#import main

from discord.ext import commands

token = "MTEwNTIzMzE1MDg3MjkyNDI3MQ.GUQuhj.EYvH4rC3ei1BhdKK_vSqtR1hKJo01KxFmubctk"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


"""
All the events must be a coroutine. If they aren’t, 
then you might get unexpected errors. In order to 
turn a function into a coroutine they must be async
 def functions.
"""

users = []

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user.name} \n ---------')
    for i in bot.get_all_members():
        users.append()

@bot.event
async def on_member_join(member):
    users.append(member)

@bot.command()
async def members(ctx):
    for i in users:
        await ctx.send(i)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)