import discord ##interface to discord
import os ##token is stored as a enviro var
import random ##need some randomness
import nekos ##handels the random gifs from website. see their github for more info
import praw
##import logging

from discord.ext import commands


token = os.environ['TOKEN']

client_id= os.environ['CLIENTID']
client_secret = os.environ['CLIENTSECRET']
reddit_password = os.environ['PASSWORD']
reddit_username = os.environ['USERNAME']

print(token)

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=reddit_password, username = reddit_username, user_agent = "kawaiibad bot, admin:cppisnice")

#nicknames = open('nicknames.txt','r') ##used for the nicknames command (with statement)
#nicknameslist = nicknames.read().splitlines() ##loads it into memory as a list
#nicknames.close() ##garbage collecting

bot = commands.Bot(command_prefix = "+&") #creates a bot
bot_color = discord.Color(value=int('7D78F3', 16))

help_text = [["ping", "Pong"], ##will be replaced with a config file at somepoint
			["botserver", "My home is here"],
			["neko", "NEKO NEKO NEE!"],
			["f", "put a f in the chat"],
			["cookie", "someone wants cookies"],
			["pat", "someone really wants a pat"],
			["kiss", "give someone a nice kiss"],
			["huh", "give a hug to someone in need"],
			["ratewaifu", "Rates your waifu"],
			["hentai", "you are a kinky person so heres some kinky stuff"],
			["nsfw_neko", "a nsfw gif of a neko cause why not"],
			["cat", "who doesnt want an image of a cat?"]]


@bot.remove_command("help")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="+&help"))

@bot.command()
async def help(ctx): ##help text to a dm
	usr =ctx.author
	message_text = '```'
	for item in help_text:
		message_text += str(item[0]) + str((20-len(item[0]))*" ") + str(item[1]) + "\n"
	await usr.send((message_text + "```"))

@bot.command() ##good debug tool
async def ping(ctx):
    await ctx.send("pong\n")

@bot.command() ##here becase the old one had it
async def botserver(ctx):
	await ctx.send("do you really think I have a sever? bruh")

@bot.command()
async def neko(ctx): ##pulls random neko from site that the og used
	imageurl = nekos.img('neko')
	embed = discord.Embed(color = bot_color)
	embed.set_image(url=imageurl)
	await ctx.send(embed= embed)

@bot.command() ##puts f in the chat with the
async def f(ctx, *, arg: str):	##todo: spaces will/are issue.
	await ctx.send(ctx.author.mention + "has paid their respects for " + str(arg))

@bot.command() ##gives a cookie to {user}
async def cookie(ctx, member: discord.Member):
	message ="**" + member.mention +"**, you got a :cookie: from **"+ ctx.author.mention + "**\n"
	embed = discord.Embed(color = bot_color, description = message)
	await ctx.send(embed = embed)

@bot.command() ##you are a baka
async def baka(ctx):
	imageurl = nekos.img("baka")
	embed = discord.Embed(color = bot_color)
	embed.set_image(url=imageurl)
	await ctx.send(embed = embed)

@bot.command() ##pats a given user
async def pat(ctx, member: discord.Member):
	if(ctx.author == member):
		embed = discord.Embed(color = bot_color, description = ("**" + member.mention + "**, you have patted yourself"))
	else:
		imageurl = nekos.img("pat")
		message = "**" + member.mention + "** you got pat by **" + ctx.author.mention + "**"
		embed = discord.Embed(color = bot_color, description = message)
		embed.set_image(url=imageurl)
	await ctx.send(embed = embed)

@bot.command() ##kisses a given user
async def kiss(ctx, member: discord.Member):
	if(ctx.author == member):
		embed = discord.Embed(color = bot_color, description = 'stop being lonely and go kiss someone')
	else:
		imageurl = nekos.img('kiss')
		message = "**" + member.mention + "** you got kissed by **" + ctx.author.mention + "**"
		embed = discord.Embed(color = bot_color, description = message)
		embed.set_image(url=imageurl)
	await ctx.send(embed = embed)

@bot.command() ##hugs a given user
async def hug(ctx, member: discord.Member):
	if(ctx.author == member):
		embed = discord.embed(color = bot_color, description = "You dont need to hug yourself, find someone else to hug")
	else:
		imageurl = nekos.img('hug')
		message = "**" + member.mention + "** you got hugged by **" + ctx.author.mention + "**"
		embed = discord.Embed(color = bot_color, description = message)
		embed.set_image(url=imageurl)
	await ctx.send(embed = embed)

"""@bot.command() ##i am stupid and so this gives me a randm nickname ingore this
async def nickname(ctx):
	message = "nickname choosen is " + str(nicknameslist[random.randint(0, len(nicknameslist))])
	await ctx.send(message)
"""
@bot.command() ##about the bot
async def about(ctx):
	embed = discord.Embed(color = bot_color, type = 'rich', description = "i am kawaiibad +&help")
	await ctx.send(embed=embed)

@bot.command() ##gives the link to the github for this bot
async def githublink(ctx):
	await ctx.send("https://github.com/chapstick404/kawaiibad")

@bot.command() ##give a given user a hug
async def cuddle(ctx, member: discord.Member):
	if(ctx.author == member): ##noone needs to cuddle themselves  this should hannel the logic for this 
		embed = discord.Embed(color = bot_color, description = "You shouldnt cuddle yourself you should go find some one")
	else:
		imageurl = nekos.img("cuddle")
		message = "**" + member.mention + "** you have received a cuddle from **" + ctx.author.mention + "**"
		embed = discord.Embed(color = bot_color, description = message)
		embed.set_image(url=imageurl)
	await ctx.send(embed=embed) 

@bot.command()
async def ratewaifu(ctx, *args):
	if len(args) < 1:
		embed = discord.Embed(color = bot_color, type = "rich", description = "You have to rate something..?")
	else:
		waifurate = int(random.choices(range(30,90,10), cum_weights=(1,3,6,10.5,13.75,16.25))[0]) + int(random.randint(0,9))
		embed = discord.Embed(color = bot_color, type = "rich", description = " I'd rate `" + args[0] + "` a " + str(waifurate))
	await ctx.send(embed = embed)

@bot.command()
async def dev_command(ctx, *args):
	if "channel_info" in args:
		await ctx.send("info: " + ctx.channel.name +"\n" + str(ctx.channel.is_nsfw()) + "\n" + str(ctx.channel.type) + "\n" + str(ctx.guild))

@bot.command()
async def hentai(ctx):
	if(ctx.channel.is_nsfw()):
		imageurl = nekos.img("random_hentai_gif")
		embed = discord.Embed(color = bot_color, description="here you go you kinky fuck")
		embed.set_image(url=imageurl)
		await ctx.sent(embed=embed)
	else:
		embed = discord.Embed(color = bot_color, description="can not send nsfw messages in this channel")
		await ctx.send(embed=embed)

@bot.command()
async def nsfw_neko(ctx):
	if(ctx.channel.is_nsfw()):
		embed = discord.Embed(color = bot_color, description = "*sigh* here you go.")
		embed.set_image(url = nekos.img("nsfw_neko_gif"))
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(color = bot_color, description="cannot send nsfw messages in this channel")
		await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
	embed = discord.Embed(color = bot_color, description="an image of a cat")
	embed.set_image(url=nekos.cat())
	await ctx.send(embed=embed)

@bot.command()
async def user(ctx):
	info = [["name", ctx.author.name],
			["friend", str(ctx.author.is_friend())]
			]
	for item in info:
		message += item[0] + ":" + item[1] + "\n"
	info_embed = discord.Embed(color = bot_color, description = message)
	info_embed.set_thumbnail(ctx.author.avatar_url)
	await ctx.send(embed=info_imbed)
	

@bot.event
async def on_message(message):
	
	if message.author != bot.user: ##logic to stop the bot from responding to itself
		if message.mention_everyone == False: ##cant have bot responding to @everyone
			if bot.user in message.mentions: 
				await message.channel.send("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!") ##how dare some one ping the bot
		await bot.process_commands(message) ##modifying this method so we need to run commands

bot.run(token)

