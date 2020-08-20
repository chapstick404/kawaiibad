import discord
import os
import random
import urllib

from discord.ext import commands
token = os.environ['TOKEN']

neko404 = open("neko404.txt", "r") ##sets up the list of 404 error nekos
listneko404 = neko404.read().splitlines()

non404 = []
for i in listneko404:
	if i != '':
		non404.append(int(i))
listneko404 = non404
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
async def help(ctx): ##help text to a dm
	usr =ctx.author
	await usr.send("`Ping			pong\nbotserver			my home is here\nneko			NEKO NEKO NEE!`\n`f			put a f in the chat`\n`cookie			someone wants cookies`\n")

@bot.command() ##good debug tool
async def ping(ctx):
    await ctx.send('pong')

@bot.command() ##here becase the old one had it
async def botserver(ctx):
	await ctx.send('do you really think I have a sever? bruh')

@bot.command()
async def neko(ctx): ##pulls random neko from site that the og used
	message = ('https://cdn.nekos.life/neko/neko_' + str(non404[random.randint(0,len(non404))]) + '.png')
	await ctx.send(message)
	await ctx.send('if this command returned a website with a 404 error please contact chapstick404#7405')
@bot.command()
async def f(ctx, arg):
	await ctx.send((str(ctx.author)) + "has paid their respects for " + str(arg))

@bot.command()
async def cookie(ctx, arg):
	await ctx.send('**' + str(arg) + '**, you got a :cookie: from **' + str(ctx.author) + '**')

bot.run(token)

