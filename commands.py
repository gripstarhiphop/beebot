import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from sys import platform

guildIDs = [929594969000390696, 580587544287379456, 340253890643755009, 765005927619231774, 691147057796218905, 389113239159439361, 621423558886817820, 943741853239492688, 1040888019906994186]


class Commands(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot
        if platform.startswith("lin"):
            self.path = "/root/serverkitten/media/"
        else:
            self.path = "./media/"


    @slash_command(name = "ping", description = "PONG! 🏓")
    async def ping(self, ctx: commands.Context):
        await ctx.respond("https://tenor.com/view/clussy-clan-funny-get-real-gif-22229968")

    @slash_command(name = "turnup", description = "turn it up!")
    async def turnup(self, ctx: commands.Context):
        await ctx.respond("https://tenor.com/view/turnip-turns-up-turnipup-zamsire-dancing-turnip-smiling-gif-21484295")

    @slash_command(name = 'av', description = "shows a user's avatar")
    async def av(self, ctx: commands.Context, member: Option(discord.Member, "Discord Member", required = False)):

        if member is None:
            member = ctx.author

        av = member.display_avatar.url
        embed = discord.Embed(title=f"**{member.name}'s Avatar**", description=f"in {member.guild.name}", color=0xFFC500)
        embed.set_image(url=av)
        await ctx.respond(embed=embed)


    

    
    # @slash_command(name = 'spotify', description = "shows a user's Spotify activity", guild_ids = guildIDs)
    # async def spotify(self, ctx: commands.Context, member: Option(discord.Member, "Discord Member", required = False)):

    #     if member is None:
    #         member = ctx.author
    #     if member.activities != :
    #         await ctx.respond("That user currently does not have a Spotify activity!")
    #         return
    #     else:
    #         spot = member.discord.Activity.Spotify
    #         embed = discord.Embed(title=f"**{member.name} is currently listening to:**", description=f"", color=0xFFC500)
    #         embed.add_field(name="Song name:", value=f'{spot.name}', inline=False)
    #         embed.add_field(name="Album name:", value=f'{spot.album}', inline=False)
    #         embed.add_field(name="Artist name:", value=f'{spot.artist}', inline=False)
    #         jacket = spot.album_cover_url
    #         embed.set_image(url=jacket)
    #         embed.add_field(name="Listen here:", value=f'{spot.track_url}', inline=False)
    #         await ctx.respond(embed=embed)




    # @slash_command(name = "changelog", description = "view the most recent changes to Bee Bot", guild_ids = guildIDs)
    # async def changelog(self, ctx):
    #     embed = discord.Embed(title=f"**Bee Bot Changelog**", description=f"Most Recent Updates to Bee Bot", color=0xFFC500)
    #     embed.add_field(name = "2/8/2022", value = "-swapped out rank embed for card, background coming soon\n-fixed bug with xp gain system", inline = False)
    #     embed.add_field(name = "2/7/2022", value = "-rolled out minor bugfix for blackjack\n-added XP for voice channel activity in Oh Look Home server\n-rolled out additonal bugfixes for blackjack\n-fixed bug for first time users in russian roulette", inline = False)
    #     embed.add_field(name = "2/3/2022", value = "-added in levelling roles \n-added in checks to transition users between the different roles  \n-All database tables reset \n-fixes rolled out for deposit and withdraw for owners\n-bossroulette added for owners\n-gamblingstats embed added", inline = False)
    #     embed.add_field(name = "2/2/2022", value = "-fixed pingpong, rolled out russian roulette role assignment fix", inline = False)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
    #     await ctx.respond(embed=embed)


    @slash_command(name = "serverstats", description = "view stats for the server you run this command in")
    async def serverstats(self, ctx):
        embed = discord.Embed(title=f"**{ctx.guild.name} Statstics**", description=f"Statistics for the current server", color=0xFFC500)
        embed.add_field(name = "**SERVER ID**", value = f"{ctx.guild.id}", inline = True)
        embed.add_field(name = "**SERVER MEMBER TOTAL**", value = f"{ctx.guild.member_count}", inline = True)
        embed.add_field(name = "**SERVER REGION**", value = f"{ctx.guild.region}", inline = True)
        embed.add_field(name = "**SERVER OWNER**", value = f"{ctx.guild.owner}", inline = True)
        embed.add_field(name = "**SERVER NITRO BOOST ROLE**", value = f"{ctx.guild.premium_subscriber_role}", inline = True)
        embed.add_field(name = "**SERVER NITRO BOOSTERS**", value = f"{ctx.guild.premium_subscription_count}", inline = True)
        embed.add_field(name = "**SERVER NITRO BOOST LEVEL**", value = f"{ctx.guild.premium_tier}", inline = True)
        embed.add_field(name = "**SERVER CREATION TIME**", value = f"{ctx.guild.created_at}", inline = True)
        # embed.set_thumbnail(ctx.guild.icon)
        await ctx.respond(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))