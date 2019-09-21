# bot.py
import os
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.voice_client import VoiceClient
import pyautogui
import pickle
from PIL import Image
import asyncio
TOKEN = "NjIwNTgwNjAzMDM2Njk2NTc5.XXZlzg.TrrGbswpWFhkQrUVPzWJbSmDlHI"
GUILD = "Self-Help Group For The Criminally Devient"
#cursedword function
with open("test.txt", "rb") as fp:   # Unpickling
     cursedword = pickle.load(fp)
print(cursedword)
client = discord.Client()
client = commands.Bot(command_prefix='$')
#rps
duels=[]
#scenarios when player 1 wins
duel_bible = {
			"r":"s",
			"s":"p",
			"p":"r"
			}
class Duelrps:

    def __init__(
        self,
        duelist1,
        duelist2,
        channel,
        input1=None,
        input2=None,
        ):
        self.user1 = duelist1
        self.user2 = duelist2
        self.input1 = input1
        self.input2 = input2
        self.channel = channel
    def logic(self):
        print(self.input1, self.input2)
        if self.input1 == self.input2:
            return 2

        for key, value in duel_bible.items():
            if (self.input1,self.input2) == (key ,value):
                return 3
        return 4
    
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    #to change status
    game = discord.Game("with my uncle in the basement")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    #currently, the reaction feature is hard coded only for a specific discord server
    channelz = discord.utils.get(client.get_all_channels(),guild__name=GUILD,name='avengers')
    #purges and sends a message along with a reaction
    def is_me(m):
     return m.author == client.user
    deleted = await channelz.purge(limit=100)
    await channelz.send('react to this for avengers')
    msg = channelz.last_message
    time.sleep(4)
    await msg.add_reaction("\U0001f534")
    OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

    #currently is redundant as there is no music feature
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
   
   
        
#gives and removes the "avengers role" upon reaction/ removal of reaction
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
@client.command()
async def test(ctx, arg):
    print("debug4")
    await ctx.send(arg)
@client.command()
async def rps(ctx, arg):
	if ctx.channel.type == discord.ChannelType.private:
		print("debugprivate")
		userx = ctx.channel.recipient
		if arg != 'r' and arg != 'p' and arg != 's':
			await ctx.channel.send('r or p or s bruh...')
			return
		time.sleep(1)
		for i in duels:
			if i.user1 == userx:
				i.input1 = arg
				if i.input2 == None:
					await ctx.channel.send("awaiting other user's input")
					return
				if i.logic() == 2:
					await i.channel.send("it's a tie folks")
				if i.logic() == 3:
					await i.channel.send(f"{i.user1.name}'s {i.input1} won, against {i.user2.name}'s {i.input2}")
				if i.logic() == 4:
					await i.channel.send(f"{i.user1.name}'s {i.input1} lost, against {i.user2.name}'s {i.input2}")
				duels.remove(i)
				return
			if i.user2 == userx:
				i.input2 = arg
				if i.input1 == None:
					await ctx.channel.send("awaiting other user's input")
					return
				if i.logic() == 2:
					await i.channel.send("it's a tie folks")
				if i.logic() == 3:
					await i.channel.send(f"{i.user1.name}'s {i.input1} won, against {i.user2.name}'s {i.input2}")
				if i.logic() == 4:
					await i.channel.send(f"{i.user1.name}'s {i.input1} lost, against {i.user2.name}'s {i.input2}")
				duels.remove(i)
				return
		await ctx.channel.send("you are not in a duel..")
		return
	member1 = await commands.MemberConverter().convert(ctx, arg)
	if member1 in ctx.guild.members:
		pass
	else:
		await ctx.channel.send("*$rps @user*")
		return
    ##rps`
	user1 = ctx.message.author
    ##debugging
	user2= member1
	if user1 == user2:
		await ctx.channel.send("you can't play rps with yourself... but I'll play with you uwu(FEATURE TO BE ADDED)")
		return
	for i in duels:
		if (i.user1 == user1) or (i.user2 == user2):
			await ctx.channel.send("*one of the users is already in a duel*")
			return
	await user1.send("Hello, please reply with either an $rps r,p or s.(representing rock,paper and sisscors respectively)")
	await user2.send("Hello, please reply with either an $rps r,p or s.(representing rock,paper and sisscors respectively)")
	await ctx.send(f"you have been challenged by {ctx.author.mention}, {member1.mention}. check your DMs")
	x = Duelrps(user1,user2,ctx.channel)
	print(x.user1)
	duels.append(x)
@client.event
async def on_message(message):
    if message.channel.type == discord.ChannelType.private:
        print("debugE")
        if message.content == '$rps':
           return
        await client.process_commands(message)
        return
    #connects the bot to the user's voice channel...
    member = message.author
    if message.author == client.user:
        return
    if message.content == 'mr stark i dont feel so good':
        role = discord.utils.get(member.guild.roles,name="avengers")
        if role in message.author.roles:
            channel = message.author.voice.channel
            await channel.connect()
        return
    #kicks player if they do not have the "avengers" role upon saying any word in the list
    global cursedword
    if message.content in cursedword:
        member = message.author
        await message.channel.send('please do not say '+message.content+' in my chirstian minecraft server you fucking degenerate'+'<@'+str(member.id)+'>')
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
    #detects a color change on the pixel where the mouse is
    #TODO:PORT CURSED SERIES AND WATCH HOTS INTO COMMANDS
    if message.content == '$watch hots':
        await message.channel.send("watching")
        im = pyautogui.screenshot()
        pix = pyautogui.position()
        ogpix = im.getpixel(pix)
        while im.getpixel(pix)==ogpix:
              time.sleep(2)
              im = pyautogui.screenshot()
              pix = pyautogui.position()
              print("pix")
        await message.channel.send(f"wake the fuck up, {message.author.mention}")
        return
    if message.content == '$powerword:cleanse':
        while len(cursedword)>2:
            del cursedword[2]
        with open("test.txt", "wb") as fp:   #Pickling
                pickle.dump(cursedword, fp)
            
    if message.content.startswith('$cursedword'):
        if len(message.content) == 11:
           await message.channel.send(cursedword)
        elif message.content.find(':') != -1:
           addcword = message.content.split(':',1)[1]
           if addcword in cursedword:
               return
           if len(cursedword) == 100:
               return
           await message.channel.send("added "+addcword+" into cursed words")
           cursedword.append(addcword)
           with open("test.txt", "wb") as fp:   #Pickling
                pickle.dump(cursedword, fp)
           with open("test.txt", "rb") as fp:   # Unpickling
                cursedword = pickle.load(fp)
        
        return
    await client.process_commands(message)

client.run(TOKEN)
