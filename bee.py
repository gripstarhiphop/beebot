import discord
from discord.ext import commands

intents = intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '~', intents = intents, case_insensitive=True, activity=discord.Activity(type=discord.ActivityType.watching, name="you bee cringe"))

@bot.event
async def on_ready():
    print("I am online")
    

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("please type an actual command")

extensions = ("reading", "reactroles", "moderation", "commands", "currency", "casino", "stats", "wordle", "beeboard", "welcome", "poll")
for extension in extensions:
    bot.load_extension(extension)
token = 'OTI0NDY1NDk1MDQ5MTQyMjcz.Yce9lQ.e-MwlxQAKvoolYyyokAq6CuBPPM'
bot.run(token)