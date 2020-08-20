import discord
import os
import random
import urllib
import nekos

from discord.ext import commands
token = os.environ['TOKEN']

bot = commands.Bot(command_prefix = '+&')
@bot.remove_command('help')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="+& help"))

@bot.command()
async def help(ctx): ##help text to a dm
	usr =ctx.author
	await usr.send("```Ping			pong\nbotserver			my home is here\nneko			NEKO NEKO NEE!\nf			put a f in the chat\ncookie			someone wants cookies```\n")

@bot.command() ##good debug tool
async def ping(ctx):
    await ctx.send('pong')

@bot.command() ##here becase the old one had it
async def botserver(ctx):
	await ctx.send('do you really think I have a sever? bruh')

@bot.command()
async def neko(ctx): ##pulls random neko from site that the og used
	message = nekos.img('neko')
	await ctx.send('```' + message '```')

@bot.command()
async def f(ctx, arg):
	await ctx.send((str(ctx.author)) + "has paid their respects for " + str(arg))

@bot.command()
async def cookie(ctx, arg):
	await ctx.send('**' + str(arg) + '**, you got a :cookie: from **' + str(ctx.author) + '**')

bot.run(token)

