import discord, datetime
from discord.commands import slash_command, Option
from discord.ext import commands
from sys import platform

class Beeboard(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot
        if platform.startswith("lin"):
            self.path = "/root/serverkitten/media/"
        else:
            self.path = "./media/"


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        emoji = payload.emoji.name
        if emoji != '📌':
            return
        guildlist = [943741853239492688, 929594969000390696, 580587544287379456, 340253890643755009]
        channellist = [959680910561804309, 959662476675387422, 960465657227542548, 961163182007808030]
        member = payload.member
        guild = member.guild
        guildFound = False
        guildnum = 0
        i = 0
        for target in guildlist:
            if target == guild.id:
                guildFound = True
                guildnum = i
            i = i + 1
        if guildFound == False:
            return
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reactionCount = 0
        for reaction in message.reactions:
            if reaction.emoji == '📌':
                reactionCount = reaction.count


        if reactionCount == 5 or (guild.id == 943741853239492688 and reactionCount == 3):
            
            boardchannel = await self.bot.fetch_channel(channellist[guildnum])
            embed = discord.Embed(title = f"This message has been pinned to the Bee Board!", description = f"{message.content}", color = 0xFFC500, timestamp=datetime.datetime.now())
            embed.add_field(name="Jump to Message", value=f"[Click Here]({message.jump_url})", inline=False)
            embed.set_author(name=f"{message.author}", icon_url = message.author.avatar.url)
            embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
            await boardchannel.send(embed=embed)
        
        
def setup(bot: commands.Bot):
    bot.add_cog(Beeboard(bot))