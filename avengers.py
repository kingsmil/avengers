# bot.py
import os
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.voice_client import VoiceClient
import pyautogui
from PIL import Image
import asyncio
TOKEN = "token"
GUILD = "Self-Help Group For The Criminally Devient"

client = discord.Client()
print('<@&617381612451135488>')
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    game = discord.Game("with my uncle in the basement")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    channelz = discord.utils.get(client.get_all_channels(),guild__name=GUILD,name='avengers')
    def is_me(m):
     return m.author == client.user
    deleted = await channelz.purge(limit=100)
    await channelz.send('react to this for avengers')
    msg = channelz.last_message
    time.sleep(2)
    await msg.add_reaction("\U0001f534")
    OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


    def load_opus_lib(opus_libs=OPUS_LIBS):
        if opus.is_loaded():
           print("opus is working?")
           return True

        for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

            raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
   
   
        
    
@client.event
async def on_reaction_add(reaction, user):
    print("debug1")
    channelz = discord.utils.get(client.get_all_channels(), guild__name=GUILD, name='avengers' )
    print(channelz.name)
    if reaction.message.channel != channelz:
         print("debug2")
         return
    if str(reaction.emoji) == "\U0001f534":
         print("debug3")
         member = user
         test = discord.utils.get(member.guild.roles, name="avengers")
         await member.add_roles(test)
@client.event
async def on_reaction_remove(reaction, user):
    channelz = discord.utils.get(client.get_all_channels(),guild__name=GUILD,name='avengers')
    print(channelz.name)
    if reaction.message.channel != channelz:
         print("debug2")
         return
    if str(reaction.emoji) == "\U0001f534":
         print("debug3")
         member = user
         test = discord.utils.get(member.guild.roles, name="avengers")
         await member.remove_roles(test)
@client.event
async def on_message(message):
    member = message.author
    if message.author == client.user:
        return
    if message.content == 'mr stark i dont feel so good':
        role = discord.utils.get(member.guild.roles,name="avengers")
        if role in message.author.roles:
            channel = message.author.voice.channel
            await channel.connect()
        return
    if message.content == 'nigger':
        member = message.author
        await message.channel.send('please do not say nigger in my chirstian minecraft server you fucking degenerate'+'<@'+str(member.id)+'>')
        test = discord.utils.get(member.guild.roles, name="avengers")
        if member in test.members:
            await message.channel.send(f'oh sorry, didnt realize you were an {test.name}')
            return
        for i in range(3):
            await message.channel.send('be purged in '+str(3-i))
            time.sleep(1)
        await member.kick()
        return
    test = discord.utils.get(member.guild.roles, name="avengers")
    if message.content == 'avengers assemble':
        await message.channel.send(f"the world needs you, {test.mention}")
        return
    if message.content == 'help me watch hots avengers':
        await message.channel.send("watching")
        im = pyautogui.screenshot()
        pix = pyautogui.position()
        ogpix = pix
        while im.getpixel(pix)==im.getpixel(ogpix):
              time.sleep(2)
              im = pyautogui.screenshot()
              pix = pyautogui.position()
              print("pix")
        await message.channel.send(f"wake the fuck up, {message.author.mention}")
        return
client.run(TOKEN)
