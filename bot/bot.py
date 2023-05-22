import discord
import activity
import datetime
import charts
#import main

from datetime import date
from datetime import datetime
from discord.ext import commands


token = 'hi'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='>', intents=intents)

"""
All the events must be a coroutine. If they aren’t, 
then you might get unexpected errors. In order to 
turn a function into a coroutine they must be async
def functions.
"""

users = []
status: dict[str, discord.Activity] = {}
last_check: dict[str, discord.Activity] = {}

data: dict[str, list] = {}

def get_user_activity(i : discord.Member) -> discord.Activity:
    if (len(i.activities) > 0 and i.activities[0].type != discord.ActivityType.custom):
        return i.activities[0]
    else:
        return None


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user.name} \n ---------')
    for i in bot.get_all_members():
        users.append(i)
        status[i.name] = get_user_activity(i)
        last_check[i.name] = None

#why is this functionality here again?
@bot.event
async def on_member_join(member):
    users.append(member)
    status[member.name] = member.activities
    last_check[member.name] = None

@bot.check
async def memberStatus(ctx):
    """
    Rough logic outline, outputs an entry to data after every event ends. 
    """
    for i in users:
        currA = get_user_activity(i)

        last_check[i.name] = status[i.name]
        status[i.name] = currA

        if (last_check[i.name] != None and last_check[i.name].type == discord.Activity and status[i.name] == None):
            data[i.name].append(activity())

    return True
           
@bot.command()
async def members(ctx):
    for i in users:
        await ctx.send(i.name)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def info(ctx):
    for i in users:
        if (len(i.activities) > 0 and i.activities[0].type != discord.ActivityType.custom):

            #some errors with this so its just wrapped for now
            try:
                print(data[i.name])
            except:
                print("user is unknown")

            #await ctx.send(data[i.name].size())
            await ctx.send(i.activities[0].name)
        else:
            await ctx.send("no activities")

bot.run(token)