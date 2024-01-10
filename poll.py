import discord, asyncio, datetime
from discord.commands import slash_command, Option
from discord.ext import commands
from sys import platform
from discord.commands.context import ApplicationContext
from discord.ui import Button, View

guildIDs = [929594969000390696, 580587544287379456, 340253890643755009, 765005927619231774, 691147057796218905, 389113239159439361, 621423558886817820, 943741853239492688, 1040888019906994186]

class Poll(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot


    @slash_command(name='poll', description = "create a poll")
    async def poll(self, ctx: ApplicationContext, question: Option(str, "Question of poll", required=True), options: Option(int, "Number of poll options", required = True, min=2, max=5), op1: Option(str, "Option #1", required=True), op2: Option(str, "Option #2", required=True), op3: Option(str, "Option #3", required=False), op4: Option(str, "Option #4", required=False), op5: Option(str, "Option #5", required=False)):
        reactors = []
        
        onect = 0
        twoct = 0
        threect = 0
        fourct = 0
        fivect = 0
        async def onecb(interaction):
            if interaction.user.id in reactors:
                await interaction.response.defer
            else:
                reactors.append(interaction.user.id)
                nonlocal onect
                onect += 1
                embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
                embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
                embed.add_field(name=f"1️⃣: {op1}", value=f"Votes: {onect}", inline=False)
                embed.add_field(name=f"2️⃣: {op2}", value=f"Votes: {twoct}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
                nonlocal options
                if options > 2:
                    embed.add_field(name=f"3️⃣: {op3}", value=f"Votes: {threect}", inline=False)
                if options > 3:
                    embed.add_field(name=f"4️⃣: {op4}", value=f"Votes: {fourct}", inline=False)
                if options > 4:
                    embed.add_field(name=f"5️⃣: {op5}", value=f"Votes: {fivect}", inline=False)
                embed.set_footer(text="Poll status: Open")
                await interaction.response.edit_message(embed=embed, view=view)

        async def twocb(interaction):
            if interaction.user.id in reactors:
                await interaction.response.defer
            else:
                reactors.append(interaction.user.id)
                nonlocal twoct
                twoct += 1
                embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
                embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
                embed.add_field(name=f"1️⃣: {op1}", value=f"Votes: {onect}", inline=False)
                embed.add_field(name=f"2️⃣: {op2}", value=f"Votes: {twoct}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
                nonlocal options
                if options > 2:
                    embed.add_field(name=f"3️⃣: {op3}", value=f"Votes: {threect}", inline=False)
                if options > 3:
                    embed.add_field(name=f"4️⃣: {op4}", value=f"Votes: {fourct}", inline=False)
                if options > 4:
                    embed.add_field(name=f"5️⃣: {op5}", value=f"Votes: {fivect}", inline=False)
                embed.set_footer(text="Poll status: Open")
                await interaction.response.edit_message(embed=embed, view=view)
        
        async def threecb(interaction):
            if interaction.user.id in reactors:
                await interaction.response.defer
            else:
                reactors.append(interaction.user.id)
                nonlocal threect
                threect += 1
                embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
                embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
                embed.add_field(name=f"1️⃣: {op1}", value=f"Votes: {onect}", inline=False)
                embed.add_field(name=f"2️⃣: {op2}", value=f"Votes: {twoct}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
                nonlocal options
                if options > 2:
                    embed.add_field(name=f"3️⃣: {op3}", value=f"Votes: {threect}", inline=False)
                if options > 3:
                    embed.add_field(name=f"4️⃣: {op4}", value=f"Votes: {fourct}", inline=False)
                if options > 4:
                    embed.add_field(name=f"5️⃣: {op5}", value=f"Votes: {fivect}", inline=False)
                embed.set_footer(text="Poll status: Open")
                await interaction.response.edit_message(embed=embed, view=view)

        async def fourcb(interaction):
            if interaction.user.id in reactors:
                await interaction.response.defer
            else:
                reactors.append(interaction.user.id)
                nonlocal fourct
                fourct += 1
                embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
                embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
                embed.add_field(name=f"1️⃣: {op1}", value=f"Votes: {onect}", inline=False)
                embed.add_field(name=f"2️⃣: {op2}", value=f"Votes: {twoct}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
                nonlocal options
                if options > 2:
                    embed.add_field(name=f"3️⃣: {op3}", value=f"Votes: {threect}", inline=False)
                if options > 3:
                    embed.add_field(name=f"4️⃣: {op4}", value=f"Votes: {fourct}", inline=False)
                if options > 4:
                    embed.add_field(name=f"5️⃣: {op5}", value=f"Votes: {fivect}", inline=False)
                embed.set_footer(text="Poll status: Open")
                await interaction.response.edit_message(embed=embed, view=view)

        async def fivecb(interaction):
            if interaction.user.id in reactors:
                await interaction.response.defer
            else:
                reactors.append(interaction.user.id)
                nonlocal fivect
                fivect += 1
                embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
                embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
                embed.add_field(name=f"1️⃣: {op1}", value=f"Votes: {onect}", inline=False)
                embed.add_field(name=f"2️⃣: {op2}", value=f"Votes: {twoct}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
                nonlocal options
                if options > 2:
                    embed.add_field(name=f"3️⃣: {op3}", value=f"Votes: {threect}", inline=False)
                if options > 3:
                    embed.add_field(name=f"4️⃣: {op4}", value=f"Votes: {fourct}", inline=False)
                if options > 4:
                    embed.add_field(name=f"5️⃣: {op5}", value=f"Votes: {fivect}", inline=False)
                embed.set_footer(text="Poll status: Open")
                await interaction.response.edit_message(embed=embed, view=view)

        async def stopcb(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer
            else:
                embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
                embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
                embed.add_field(name=f"1️⃣: {op1}", value=f"Votes: {onect}", inline=False)
                embed.add_field(name=f"2️⃣: {op2}", value=f"Votes: {twoct}", inline=False)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
                nonlocal options
                if options > 2:
                    embed.add_field(name=f"3️⃣: {op3}", value=f"Votes: {threect}", inline=False)
                if options > 3:
                    embed.add_field(name=f"4️⃣: {op4}", value=f"Votes: {fourct}", inline=False)
                if options > 4:
                    embed.add_field(name=f"5️⃣: {op5}", value=f"Votes: {fivect}", inline=False)
                view.disable_all_items()
                
                embed.set_footer(text="Poll status: Closed")
                await interaction.response.edit_message(embed=embed, view=view)

                
        
        embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
        embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
        embed.add_field(name=f"1️⃣: {op1}", value="Votes: 0", inline=False)
        embed.add_field(name=f"2️⃣: {op2}", value="Votes: 0", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png")
        if options > 2:
            embed.add_field(name=f"3️⃣: {op3}", value=f"Votes: 0", inline=False)
        if options > 3:
            embed.add_field(name=f"4️⃣: {op4}", value=f"Votes: 0", inline=False)
        if options > 4:
            embed.add_field(name=f"5️⃣: {op5}", value=f"Votes: 0", inline=False)
        embed.set_footer(text="Poll status: Open")

        onebtn = Button(label=f"{op1}", style=discord.ButtonStyle.blurple, emoji="1️⃣")
        twobtn = Button(label=f"{op2}", style=discord.ButtonStyle.blurple, emoji="2️⃣")
        threebtn = Button(label=f"{op3}", style=discord.ButtonStyle.blurple, emoji="3️⃣")
        fourbtn = Button(label=f"{op4}", style=discord.ButtonStyle.blurple, emoji="4️⃣")
        fivebtn = Button(label=f"{op5}", style=discord.ButtonStyle.blurple, emoji="5️⃣")
        stopbtn = Button(label=f"End Poll", style=discord.ButtonStyle.danger, emoji="🛑")
        onebtn.callback = onecb
        twobtn.callback = twocb
        threebtn.callback = threecb
        fourbtn.callback = fourcb
        fivebtn.callback = fivecb
        stopbtn.callback = stopcb

        view = View(timeout=None)
        view.add_item(onebtn)
        view.add_item(twobtn)
        if options > 2:
            view.add_item(threebtn)
        if options > 3:
            view.add_item(fourbtn)
        if options > 4:
            view.add_item(fivebtn)
        view.add_item(stopbtn)
        await ctx.respond("Poll created!")
        msg = await ctx.send(embed=embed, view=view)


    # @slash_command(name='poll', description = "create a poll", guild_ids = guildIDs)
    # async def poll(self, ctx: ApplicationContext, question: Option(str, "Question of poll", required=True), options: Option(int, "Number of poll options", required = True, min=2, max=5), op1: Option(str, "Option #1", required=True), op2: Option(str, "Option #2", required=True), op3: Option(str, "Option #3", required=False), op4: Option(str, "Option #4", required=False), op5: Option(str, "Option #5", required=False)):
        
    #     embed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
    #     embed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
    #     embed.add_field(name=f"1️⃣: {op1}", value="Current votes: 0", inline=False)
    #     embed.add_field(name=f"2️⃣: {op2}", value="Current votes: 0", inline=False)
    #     embed.set_footer(text="Poll status: Open", icon_url='https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
    #     emojilist = ["3️⃣", "4️⃣", "5️⃣"]
    #     if options > 2:
    #         i = 0
    #         while i + 2 <= options:
    #             opstring = f"op{i + 2}"
    #             embed.add_field(name=f"{opstring}", value=f"Current votes: 0", inline=False)
    #     await ctx.respond("poll created!")
    #     msg = await ctx.send(embed=embed)
    #     await msg.add_reaction('1️⃣')
    #     await msg.add_reaction('2️⃣')
    #     await msg.add_reaction('🛑')
    #     onect = 0
    #     twoct = 0
    #     threect = 0
    #     fourct = 0
    #     fivect = 0

    #     pollover = False
    #     reactors = []
    #     while pollover == False:
    #         def check(reaction, user):
    #             return reaction.message == msg and user.bot == False
    #         try:
    #             react, user = await self.bot.wait_for('reaction_add', check=check, timeout=3600)
    #         except asyncio.TimeoutError:
    #             closebed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
    #             closebed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
    #             closebed.add_field(name=f"1️⃣: {op1}", value=f"Current votes: {onect}", inline=False)
    #             closebed.add_field(name=f"2️⃣: {op2}", value=f"Current votes: {twoct}", inline=False)
    #             closebed.set_footer(text="Poll status: Closed", icon_url='https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
    #             await msg.edit(embed=closebed)
    #             pollover = True
    #         if str(react.emoji) == str('🛑'):
    #             if user.id == ctx.author.id:
    #                 closebed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
    #                 closebed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
    #                 closebed.add_field(name=f"1️⃣: {op1}", value=f"Current votes: {onect}", inline=False)
    #                 closebed.add_field(name=f"2️⃣: {op2}", value=f"Current votes: {twoct}", inline=False)
    #                 closebed.set_footer(text="Poll status: Closed", icon_url='https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
    #                 await msg.edit(embed=closebed)
    #                 pollover = True
    #             else:
    #                 continue
    #         elif str(react.emoji) == str('1️⃣'):
    #             if user.id in reactors:
    #                 continue
    #             else:
    #                 reactors.append(user.id)
    #                 onect = onect + 1
    #                 closebed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
    #                 closebed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
    #                 closebed.add_field(name=f"1️⃣: {op1}", value=f"Current votes: {onect}", inline=False)
    #                 closebed.add_field(name=f"2️⃣: {op2}", value=f"Current votes: {twoct}", inline=False)
    #                 closebed.set_footer(text="Poll status: Open", icon_url='https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
    #                 await msg.edit(embed=closebed)
    #                 continue
    #         elif str(react.emoji) == str('2️⃣'):
    #             if user.id in reactors:
    #                 continue
    #             else:
    #                 reactors.append(user.id)
    #                 twoct = twoct + 1
    #                 closebed = discord.Embed(title="**Bee Bot Poll**", description=f"{question}", timestamp=datetime.datetime.utcnow(), color=0xFFC500)
    #                 closebed.set_author(name=f"Created by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
    #                 closebed.add_field(name=f"1️⃣: {op1}", value=f"Current votes: {onect}", inline=False)
    #                 closebed.add_field(name=f"2️⃣: {op2}", value=f"Current votes: {twoct}", inline=False)
    #                 closebed.set_footer(text="Poll status: Open", icon_url='https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
    #                 await msg.edit(embed=closebed)
    #                 continue

        


       

def setup(bot: commands.Bot):
    bot.add_cog(Poll(bot))