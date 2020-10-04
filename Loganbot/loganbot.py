import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random

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
	activity = discord.Game(name="bot")
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
async def comfort(ctx, *, user):
	image = os.listdir('./cogs/comfort/')
	imgString = random.choice(image)
	path = "./cogs/comfort/" + imgString
	await ctx.send(f'{ctx.message.author.mention} comforted {user}!', file=discord.File(path))

client.run('NzQ4NjgzMzE0MTIyMTk1MTI0.X0g_qw.ChCHzkf-qOsG-YYNJc_nqYE8Z0A') 