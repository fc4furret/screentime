import discord
import activity
import datetime
#import main

from datetime import date
from datetime import datetime
from discord.ext import commands


token = ''

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)

"""
All the events must be a coroutine. If they aren’t, 
then you might get unexpected errors. In order to 
turn a function into a coroutine they must be async
def functions.
"""

users = []
status = [] 
last_check = []

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user.name} \n ---------')
    for i in bot.get_all_members():
        users.append(i)
        status.append(i.activities)
        last_check.append(i.activities)

    bot.dispatch("game_start", )

@bot.event
async def on_member_join(member):
    users.append(member)
    status.append(member.activities)
    last_check.append(member.activites)

@bot.check
async def memberStatus(ctx):
    global last_check
    for i in range(len(users)):
        status[i] = users[i].activities
        # not sure if unions preserve order or not but i'm going to assume they do to save me some pain
        for x in status[i]:
            if (last_check[i][0] != x):
                storage = last_check[i][0]
                last_check[i] = status[i]
                return True 
            last_check = status[i]
            return True
        
#bug fixed
    return True
           
@bot.command()
async def members(ctx):
    for i in users:
        await ctx.send(i.name)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)