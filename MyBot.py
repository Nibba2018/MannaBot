import discord
from discord.ext import commands
import random
import datetime

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def flip():
    '''Flips a Coin'''
    flip=random.choice(('Heads','Tails'))
    await bot.say(flip)

@bot.command()
async def roll():
    '''Rolls a Die'''
    roll=random.randint(1,6)
    await bot.say(roll)

@bot.command()
async def feedback(fb : str):
    '''Provide Feedback'''
    await bot.say("Thank You, for your feedback!:smile:")
    fb=fb+'\n'
    f=open('feedback.txt','a')
    f.write(fb)
    f.close()

@bot.command()
async def solve(s : str):
    '''To solve Math Expressions,Python commands,etc.''' 
    if 'os.' in message.content:
        await bot.say("Access Denied")
    else:
        await bot.say(eval(s))
        del s

@bot.command()
async def purge(n : int):
    '''Deletes Messages'''
    deleted =  await bot.purge_from(channel,limit=n)
    await bot.say('Deleted {} message(s)'.format(len(deleted)))
    
@bot.command()
async def ping():
    '''Calculates the Latency between the Manna and Discord'''
    firstmsg = await bot.say("Pinging...")
    ms = int(float(str(firstmsg.timestamp - timestamp)[-9:])*1000)
    await bot.edit_message(firstmsg,"Pong!! **{}** ms".format(int(ms/10))) #divided by 10 to manipulate

@bot.command()
async def invite():
    '''Invite Manna to your server'''
    f=open('feedback.txt','r')
    await bot.say(f.readline())
    f.close()
bot.run('MzM5NDYwMjI4MDE1ODQ5NDc0.DInG7g.fuCwLvw9V3fRnZWPqMJ00DeSBGA')
