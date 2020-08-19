import discord
from discord.ext import commands

class MyBot(commands.Bot):

bot = MyBot(command_prefix = '+&')
@bot.remove_command('help')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="+& help"))
	print('logged in as')
	print(bot.user.name)
@bot.command()
async def help(ctx):
	usr =ctx.author
	await usr.send("`Ping			pong`\n`botserver			my home is here`")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def botserver(ctx):
	await ctx.send('do you really think I have a sever? bruh')

bot.run('NzQ1NzI3NjAxNDQ3OTI3OTE5.Xz1-8w.0-rwLe9e36yXfMQ3ObZeXqyqEEI')

