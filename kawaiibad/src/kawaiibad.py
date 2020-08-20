import discord
import os
import random
import urllib
import nekos

from discord.ext import commands

token = os.environ['TOKEN']

nicknames = open('nicknames.txt','r')
nicknameslist = nicknames.read().splitlines()
nicknames.close()
bot = commands.Bot(command_prefix = '+&')

@bot.remove_command('help')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="+& help"))

@bot.command()
async def help(ctx): ##help text to a dm
	usr =ctx.author
	await usr.send("```Ping			pong\nbotserver			my home is here\nneko			NEKO NEKO NEE!\nf			put a f in the chat\ncookie			someone wants cookies\npat			someone really wants a pat\nkiss			give someone a nice kiss\nhug 				give a hug to someone in need```")

@bot.command() ##good debug tool
async def ping(ctx):
    await ctx.send('pong\n')

@bot.command() ##here becase the old one had it
async def botserver(ctx):
	await ctx.send('do you really think I have a sever? bruh')

@bot.command()
async def neko(ctx): ##pulls random neko from site that the og used
	imageurl = nekos.img('neko')
	embed = discord.Embed()
	embed.set_image(url=imageurl)
	await ctx.send(embed= embed)

@bot.command()
async def f(ctx, arg):
	await ctx.send(ctx.author.mention + "has paid their respects for " + str(arg) + '\n' + survey)

@bot.command()
async def cookie(ctx, member: discord.Member):
	await ctx.send('**' + member.mention + '**, you got a :cookie: from **' + ctx.author.mention + '**\n' + survey)

@bot.command()
async def baka(ctx):
	imageurl = nekos.img('baka')
	embed = discord.Embed()
	embed.set_image(url=imageurl)
	await ctx.send(embed = embed)
@bot.command()
async def pat(ctx, member: discord.Member):
	imageurl = nekos.img('pat')
	message = "**" + member.mention + "** you got pat by **" + ctx.author.mention + '**'
	embed = discord.Embed(description = message)
	embed.set_image(url=imageurl)
	await ctx.send(embed = embed)

@bot.command()
async def kiss(ctx, member: discord.Member):
	imageurl = nekos.img('kiss')
	message = '**' + member.mention + '** you got kissed by **' + ctx.author.mention + '**'
	embed = discord.Embed(description = message)
	embed.set_image(url=imageurl)
	await ctx.send(embed = embed)
@bot.command()
async def hug(ctx, member: discord.Member):
	imageurl = nekos.img('hug')
	message = '**' + member.mention + '** you got hugged by **' + ctx.author.mention + '**'
	embed = discord.Embed(description = message)
	embed.set_image(url=imageurl)
	await ctx.send(embed = embed)

@bot.command()
async def nickname(ctx):
	message = "nickname choosen is " + str(nicknameslist[random.randint(0, len(nicknameslist))] + '\n' + survey)
	await ctx.send(message)

@bot.command()
async def about(ctx):
	embed = discord.Embed(type = 'rich', description = "i am kawaiibad")
	await ctx.send(embed=embed)

@bot.command()
async def githublink(ctx):
	await ctx.send("https://github.com/chapstick404/kawaiibad")
##@bot.command()
##async def when_mentioned(ctx):
##	await ctx.send("REEEEEEEEEEEEE")

bot.run(token)

