import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random

client = commands.Bot(command_prefix = '.')

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
	
client.run('')
