import discord
import activity
import datetime
import charts
#import main

from quickchart import QuickChart
from datetime import date
from datetime import timezone
from datetime import datetime
from activity import activity
from charts import chart
from discord.ext import commands, tasks


token = 'hi'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

class MyBot(commands.Bot):
    @tasks.loop(seconds=5)
    async def memberStatus(ctx):
        """
        Rough logic outline, outputs an entry to data after every event ends. 
        """
        for i in users:
            currA = get_user_activity(i)

            if (status[i.name] == None and currA != None):
                backup_time[i.name] = datetime.now(timezone.utc)

            last_check[i.name] = status[i.name]
            status[i.name] = currA

            b = last_check[i.name]

            #print(last_check[i.name])
            #print(status[i.name])
            #print(' ----------------- ')

            if (last_check[i.name] != None and status[i.name] == None):
                #print(" -------------------------------------- hat") 
                if (last_check[i.name].start == None): data[i.name].append(activity(backup_time[i.name], datetime.now(timezone.utc), last_check[i.name].name))
                else: data[i.name].append(activity(last_check[i.name].start, datetime.now(timezone.utc), last_check[i.name].name))
                #data[i.name].append(1)

        print("running!")
    

bot = MyBot(command_prefix='>', intents=intents)

"""
All the events must be a coroutine. If they aren’t, 
then you might get unexpected errors. In order to 
turn a function into a coroutine they must be async
def functions.
"""

users = []
status: dict[str, discord.Activity] = {}
last_check: dict[str, discord.Activity] = {}
backup_time: dict[str, datetime] = {}

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
        data[i.name] = []
        backup_time[i.name] = datetime.now(timezone.utc)
    bot.memberStatus.start()

@bot.event
async def on_member_join(member):
    users.append(member)
    status[member.name] = member.activities
    last_check[member.name] = None
           
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
            #await ctx.send(data[i.name].size())
            await ctx.send(i.activities[0].name)
        else:
            await ctx.send("no activities")

@bot.command()
async def show_data(ctx):
    await ctx.send(data.items())
    await ctx.send('hi there')
    #for i in users:
        #if (data.get(i.name) != None):
            #await ctx.send(data[i.name])

@bot.command()
async def chart(ctx):
    for key in users:
        activities = data[key.name]
        activity_names = []
        activity_times = []
        for i in activities:
            activity_names.append(i.name)
            activity_times.append((i.time.days * 1440) + (i.time.seconds / 60))

        qc = QuickChart()
        qc.config = {
            "type": "bar",
            "data": {
                "type": "bar",
                "labels": activity_names,
                "datasets": [{
                    "label": "screentime",
                    "data": activity_times

                }]
            }
        }

        # Print a chart URL
        #await ctx.send(key.name + ": " + qc.get_url())

        # Print a short chart URL
        await ctx.send(key.name + ": " + qc.get_short_url())

bot.run(token)