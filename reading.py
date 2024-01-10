import discord
from discord.ext import commands
from sys import platform


class Reading(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot
        


    @commands.Cog.listener()
    async def on_message(self, message):
        #deletes any server links that might get posted and warns the poster
        # if "discord.gg/" in message.content and message.guild.id == 580587544287379456 and message.content != 'discord.gg/inhouse' and "https://promos.discord.gg/"not in message.content:
        #     await message.channel.send(f"{message.author.mention} Don't post server links retard")
        #     await message.delete()

        message_content = message.content.lower()

        #reactions to messages with emojis
        if "sex" in message_content:
            emoji = '\U0001F975'
            await message.add_reaction(emoji)
        if "british" in message_content:
            emoji = '\U0001F913'
            await message.add_reaction(emoji)
        if "bald" in message_content:
            emoji = '🧑‍🦲'
            await message.add_reaction(emoji)
            #Oh Look Home suggestions channel reactions
        if message.channel.id == 862829731903700992:
            bademoji = '\U0000274C'
            goodemoji = '\U00002705'
            await message.add_reaction(goodemoji)
            await message.add_reaction(bademoji)
        #Oh Look Home This or That channel reactions
        if message.channel.id == 887130115551662080:
            yesemoji = "<:peepoyes:887132751210360883>"
            noemoji = "<:peepono:887132751063564400>"
            idkemoji = "<:peepoidk:887132750988062761>"
            await message.add_reaction(yesemoji)
            await message.add_reaction(noemoji)
            await message.add_reaction(idkemoji)
        #personally motivated
        if "gwipa" in message_content:
            await message.delete()
        if "gwippa" in message_content:
            await message.delete()

        # if message.author.id == 395614590911774733:
        #     emoji = '\U0001F913'
        #     await message.add_reaction(emoji)
        
        #checks messages for slurs and deletes them
        slurs = ("faggot", "nigger", "zipperhead", "chink")
        if any(slurs in message_content for slurs in slurs) and message.guild.id == 580587544287379456:
            await message.delete()
            await message.channel.send("watch your language, there are children in here!")
        if "https://www.twitch.tv/" in message_content and message.channel.id == 580587544287379459:
            await message.delete()
            await message.channel.send("Please post twitch links in <#695799016205713498>")

        
        # if "tyler" in message_content and message.guild.id == 580587544287379456:
        #     await message.delete()
        if "bobby" in message_content and message.guild.id == 340253890643755009:
            await message.add_reaction('🤏')
        if message_content == "https://cdn.discordapp.com/emojis/878779549037510727.gif?size=48":
            await message.delete()
        if "wah" in message_content and message.guild.id == 580587544287379456:
            rinaemoji = "<:rina:907869780990631946>"
            await message.add_reaction(rinaemoji)

        #other stuff
        # if message.author.id == 236676299308007425:
        #     frogemoji = '\U0001F438'
        #     await message.add_reaction(frogemoji)

        # if message.author.id == 799893716608876544:
        #     falconemoji = "<:falcon:921194329148649482>"
        #     await message.add_reaction(falconemoji)
        if message_content == "sup" and message.author.id == 799893716608876544:
            await message.delete()

        # if message.author.id == 563132355661791232:
        #     clownemoji = '\U0001F921'
        #     await message.add_reaction(clownemoji)
        # if message.author.id == 896545340726067200:
        #     twomomsemoji = '👩‍👩‍👦'
        #     await message.add_reaction(twomomsemoji)

        if "biscuit" in message_content and message.guild.id == 580587544287379456:
            await message.channel.send(file=discord.File("hahabiscuit.png"))
        # if message.author.id == 914010981766664212:
        #     coomemoji = "<:coom:970840687589351464>"
        #     await message.add_reaction("🇭")
        #     await message.add_reaction("🇮")
        #     await message.add_reaction("🇸")
        #     await message.add_reaction(coomemoji)
        #     await message.add_reaction("🗑️")


def setup(bot: commands.Bot):
    bot.add_cog(Reading(bot))