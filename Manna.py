import discord
import random
import math
import string
import os
import sys
import socket
import datetime


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in')
    print('Name:{}'.format(client.user.name))
    print('ID:{}'.format(client.user.id))
    print(discord.__version__)
    print('------------')
    

@client.event
async def on_message(message):
    try:
        if message.content.lower() == 'manna rocks':
            await client.add_reaction(message,'👌')
        elif message.content.lower() == '!!flip':
            flip=random.choice(('Heads','Tails'))
            await message.channel.send(flip)
        elif message.content.lower() == '!!roll':
            roll=random.randint(1,6)
            await message.channel.send(roll)
        elif message.content.lower() == '!!help':
            f=open('help.txt','r')
            await message.channel.send(f.read())
            f.close()
        elif message.content.startswith('!!feedback'):
            fb=message.content
            await message.channel.send("Thank You, for your feedback!:smile:")
            fb=fb[11:]
            fb=fb+' : '+str(datetime.datetime.now())+'\n'
            f=open('feedback.txt','a')
            f.write(fb)
            f.close()
        elif '!!aaaaa' in message.content.lower():
            Mrant='''What Culture?!!
I will give you a kick in the @$$ and you will be out of the class!! :angry:''' 
            await message.channel.send(Mrant)
        elif message.content.lower() == '!!shalini mam' or message.content == '69':
            await message.channel.send("( ͡° ͜ʖ ͡°)")
        elif message.content.startswith('!!solve'):
            s=message.content
            s=s[8:] 
            if 'os.' in message.content:
                await message.channel.send("Access Denied")
            else:
                await message.channel.send(eval(s))
            del s
        elif 'kiss' in message.content.lower():
            await message.channel.send("😘")
        elif message.content.startswith('!!purge'):
            s=message.content
            s=s[8:]
            s=int(s)
            deleted =  await client.purge_from(limit=s)
            await message.channel.send('Deleted {} message(s)'.format(len(deleted)))
            del s
        elif message.content.lower() == '!!ping':
            firstmsg = await message.channel.send("Pinging...")
            ms = int(float(str(firstmsg.timestamp - message.timestamp)[-9:])*1000)
            await client.edit_message(firstmsg, "Pong!! **{}** ms".format(int(ms/10))) #divided by 10 to manipulate
        elif message.content.lower() == '!!sensible':
            await message.channel.send("Elephant is Flying!! :elephant: :butterfly:")
        elif message.content.lower() == '!!invite':
            f=open('feedback.txt','r')
            await message.channel.send(f.readline())
            f.close()
        elif message.content.lower() == '!!time':
            t=datetime.datetime.now()
            await message.channel.send(t)
        elif message.content.startswith('!!say'):
            await client.purge_from(limit=1)
            s=message.content
            s=s[6:] 
            if 'os.' in message.content:
                await message.channel.send("Access Denied")
            else:
                await message.channel.send(eval(s))
            del s
            
            
                    
    except:
        await message.channel.send(sys.exc_info())  
        

client.run('MzQ4ODE5MjMwODgxNDgwNzA0.DHse1g.ZG4xyQR9jg9gxSsGQhtY2vprSYs')
    
