import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random
import youtube_dl
client = commands.Bot(command_prefix = '.')

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="Discord"))
	print('Bot is ready!')

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
	await ctx.send(f'Ping is {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount=0):
		await ctx.channel.purge(limit=amount + 1)
		await ctx.send(f'Deleted {amount} messages')

@purge.error
async def error(ctx, error):
	if isinstance(error, administrator=False):
		await ctx.send('Sorry you are not allowed to use this command.')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'''
		 .  .  .　　。　　　　•　 　ﾟ　　。 　　.。　. 。
		 
		 .　　　 　　.　　　　　。　　 。　. 　  . 。　.
		 
		  .　 。　.　 。　.  ඞ 。 .　 • 　　　　•  . 。
		  
		  ﾟ　　 {member} was not an Imposter. 。　.。
		  
		   '　　　 1 Impostor remains 　 　　。   .   .
		  .  .　.　　　. ,　　　　.　 .  .       .  。
	''')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f'''
		 .  .  .　　。　　　　•　 　ﾟ　　。 　　.。　. 。
		 
		 .　　　 　　.　　　　　。　　 。　. 　  . 。　.
		 
		  .　 。　.　 。　.  ඞ 。 .　 • 　　　　•  . 。
		  
		  ﾟ　　{member} was an Imposter.　 。　.。　.
		  
		   '　　　 0 Impostor remains 　 　　。   .   .
		  .  .　.　　　. ,　　　　.　 .  .       .  。
		  ''')
         

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
	 	banned_users = await ctx.guild.bans()
	 	member_name, member_discriminator = member.split('#')

	 	for ban_entry in banned_users:
	 		user = ban_entry.user

	 		if (user.name, user.discriminator) == (member_name, member_discriminator):
	 			await ctx.guild.unban(user)
	 			await ctx.send(f'{user.mention} was unbanned ඞ')
		 
@client.command()
async def love(ctx, member):
	 	await ctx.send(f'Feel the love {member} ')

@client.command()
async def league(ctx, member):
	 	await ctx.send(f'{member} Lets play league later baby gurl')

@client.command()
async def simp(ctx, member):
	 	await ctx.send(f'{member} stop simping.')

@client.command()
async def osu(ctx, member):
	 	await ctx.send(f'{member} you playing osu! baby gurl')

@client.command()
async def mc(ctx, member):
	await ctx.send(f'{member} lets play minecraft baby gurl')

@client.command()
async def comfort(ctx, *, user):
	image = os.listdir('./cogs/comfort/')
	imgString = random.choice(image)
	path = "./cogs/comfort/" + imgString
	await ctx.send(f'{ctx.message.author.mention} comforted {user}!', file=discord.File(path))

@client.command()
async def kiss(ctx, *, user):
	image = os.listdir('./cogs/kiss/')
	imgString = random.choice(image)
	path = "./cogs/kiss/" + imgString
	await ctx.send(f'{ctx.message.author.mention} kissed {user}!', file=discord.File(path))

@client.command
async def hug(ctx, *, user):
	image = os.listdir('./cogs/hug/')
	imgString = random.choice(image)
	path = './cogs/hug/' + imgString
	await ctx.send(f'{ctx.message.author.mention} huged {user}!', file=discord.File(path))

@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')
        
@client.command(name='play', help='This command plays songs')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])

@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@client.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()

client.run('NzQ4NjgzMzE0MTIyMTk1MTI0.X0g_qw.IervcTvqSJ16Bw6wX5GFrFWXuwg') 
