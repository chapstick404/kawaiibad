import discord
import os
import random
import urllib

from discord.ext import commands
token = os.environ['TOKEN']

neko404 = open("neko404.txt", "r")
listneko404 = neko404.read().splitlines()

non404 = []
for i in range(100,299):
	if i in listneko404:
		continue
	else:
		non404.append(i)

bot = commands.Bot(command_prefix = '+&')
@bot.remove_command('help')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="+& help"))
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

@bot.command()
async def neko(ctx):

	message = ('https://cdn.nekos.life/neko/neko_' + str(non404[random.randint(0,len(non404))]) + '.png')
	await ctx.send(message)
	await ctx.send('if this command returned a website with a 404 error please contact chapstick404#7405')

bot.run(token)

