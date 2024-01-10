import asyncpg, discord
from discord.ext import commands
from discord.commands import slash_command, Option
from discord.commands.context import ApplicationContext
from easy_pil import Editor, load_image_async, Font

guildIDs = [929594969000390696, 580587544287379456, 340253890643755009, 765005927619231774, 691147057796218905, 389113239159439361, 621423558886817820, 943741853239492688, 1040888019906994186]
currency_name = "BeeBucks"

class Stats(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot
        self.message_database = {}

    @slash_command(name='profile', description = "view your Bee Bot server profile")
    async def profile(self, ctx: ApplicationContext, member: Option(discord.Member, "Discord Member", required = False)):

        if member is None:
            member = ctx.author
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')

        result = await db.fetch(f"SELECT xp, lvl, coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{member.id}'")
        if result == []:
            await ctx.respond("You are not entered into the system, please send a message then try again.")
            return
        else:
            userlvl = result[0]['lvl']
            userxp = result[0]['xp']
            usercoins = result[0]['coins']
            levelxp = ((userlvl + 1) * 400 + userlvl*150 + userlvl**2) if userlvl != 0 else 400
            minuslvlxp = ((userlvl) * 400 + (userlvl-1)*150 + (userlvl-1)**2) if userlvl <= 1 else 400
            if userlvl > 0:
                percentage = ((userxp-minuslvlxp)/(levelxp-minuslvlxp))* 100
            else:
                percentage = (userxp/levelxp)* 100


            backdrop = Editor(f"/root/beebot/cards/beebotcard6.png")
            userpfp = await load_image_async(str(member.display_avatar))
            userpfp = Editor(userpfp).resize((180, 180)).circle_image()
            backdrop.paste(userpfp.image, (30, 32))
            font = Font("/usr/share/fonts/Poppins/Poppins-Black.ttf", size = 50)
            smallfont = Font("/usr/share/fonts/Poppins/Poppins-Black.ttf", size = 40)
            tinyfont = Font("/usr/share/fonts/Poppins/Poppins-Black.ttf", size = 20)
            #border for XP bar
            backdrop.bar(
            (228, 218),
            max_width=654,
            height=44,
            percentage=100,
            fill="#393941",
            radius=22,
            )
            #empty XP bar
            backdrop.bar(
            (230, 220),
            max_width=650,
            height=40,
            percentage=100,
            fill="#eeeeff",
            radius=20,
            )
            #full XP bar
            backdrop.bar(
            (230, 220),
            max_width=650,
            height=40,
            percentage=percentage,
            fill="#FFC500",
            radius=20,
            )
            #username
            backdrop.text(
                (248, 65), 
                str(member), 
                font=font, 
                color="black"
            )
            #user level
            backdrop.text(
            (48, 240),
            f"Level {userlvl}",
            font=smallfont,
            color="black",
            )
            #coins
            backdrop.text(
                (328, 150),
                f": {usercoins}",
                font=smallfont,
                color="black",
            )
            #xp ratio
            backdrop.text(
                (720, 190),
                f"XP: {userxp} / {levelxp}",
                font=tinyfont,
                color="black",
            )

            #xp ratio
            backdrop.text(
                (750, 10),
                f"Bee Bot XP Card",
                font=tinyfont,
                color="black",
            )


            file = discord.File(fp=backdrop.image_bytes, filename="beebotcard.png")
            await ctx.respond(file=file)

    @slash_command(name='leaderboard', description = "view server XP leaderboard")
    async def leaderboard(self, ctx: ApplicationContext):
        embed = discord.Embed(title=f"{ctx.guild} Leaderboard", description="", color = 0xFFC500)
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        userlist = await db.fetch(f"SELECT * FROM beelevel WHERE guild_id = '{ctx.guild.id}' ORDER BY lvl DESC, xp DESC LIMIT 10")
        emojilist = {0: ':first_place:', 1: ':second_place:', 2: ':third_place:', 3: ':four:', 4: ':five:', 5: ':six:', 6: ':seven:', 7: ':eight:', 8: ':nine:', 9: ':keycap_ten:'}
        for i,v in enumerate(userlist):
            number = emojilist[i]
            member = await self.bot.fetch_user(int(v['user_id']))
            embed.add_field(name=f'{number}: {member.name}', value = f'Level: {v["lvl"]} \nExperience: {v["xp"]} \nMessages: {v["messages"]}', inline=False)
        await ctx.respond(embed=embed)

    
    @slash_command(name='forbees', description = "view server coin leaderboard")
    async def forbees(self, ctx: ApplicationContext):
        embed = discord.Embed(title=f"{ctx.guild} Coin Leaderboard", description="", color = 0xFFC500)
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/929594997790101515/938652122285748295/beebotwbg.png')
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        userlist = await db.fetch(f"SELECT * FROM beelevel WHERE guild_id = '{ctx.guild.id}' ORDER BY coins DESC LIMIT 10")
        emojilist = {0: ':first_place:', 1: ':second_place:', 2: ':third_place:', 3: ':four:', 4: ':five:', 5: ':six:', 6: ':seven:', 7: ':eight:', 8: ':nine:', 9: ':keycap_ten:'}
        for i,v in enumerate(userlist):
            number = emojilist[i]
            member = await self.bot.fetch_user(int(v['user_id']))
            embed.add_field(name=f'{number}: {member.name}', value = f'Coins: {v["coins"]}', inline=False)
        await ctx.respond(embed=embed)
    
    
    @slash_command(name='gamblestats', description = "view your Bee Bot gambling stats")
    async def gamblestats(self, ctx: ApplicationContext, member: Option(discord.Member, "Discord Member", required = False)):

        if member is None:
            member = ctx.author
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')

        result = await db.fetch(f"SELECT bj_wins, bj_losses, ban_win_streak, best_coinflip, coinswon, coinslost FROM gamblingstats WHERE guild_id = '{ctx.guild.id}' AND user_id = '{member.id}'")
        if result == []:
            await ctx.respond("You are not entered into the system, please send a message then try again.")
            return
        else:
            bjwins = result[0]['bj_wins']
            bjlosses = result[0]['bj_losses']
            bjtotalgames = bjwins + bjlosses
            if bjtotalgames == 0:
                bjwinpct = 0
            else:
                bjwinpct = (bjwins/bjtotalgames)*100
            coinswon = result[0]['coinswon']
            coinslost = result[0]['coinslost']
            totalwinnings = coinswon - coinslost

            winstreak = result[0]['ban_win_streak']
            best_coinflip = result[0]['best_coinflip']
            embed = discord.Embed(title = f"{member.name}'s Gambling Stats in {ctx.guild.name}", description = "", color = 0xFFC500)
            embed.add_field(name="Blackjack Record", value=f'{bjwins}-{bjlosses}', inline=True)
            embed.add_field(name="Blackjack Win Percentage", value=f'{bjwinpct:.0f}%', inline=True)
            embed.add_field(name="Current Roulette Win Streak", value=f'{winstreak}', inline=True)
            embed.add_field(name=f"Total {currency_name} Won", value=f'{coinswon}', inline=True)
            embed.add_field(name=f"Total {currency_name} Lost", value=f'{coinslost}', inline=True)
            embed.add_field(name="Total Winnings", value=f'{totalwinnings}', inline=True)
            embed.add_field(name="Best Coinflip Streak", value=f'{best_coinflip}', inline=True)

            pfp = member.avatar.url
            embed.set_thumbnail(url=(pfp))
            await ctx.respond(embed=embed)


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.message_database[str(message.channel.id)] = message


    @slash_command(name='snipe', description = "see what some cringelord just deleted", guild_ids = guildIDs)
    async def snipe(self, ctx: commands.Context):
        channel = str(ctx.channel_id)
        if channel not in self.message_database.keys() or self.message_database[channel] == {}:
            await ctx.respond("There's nothing to snipe you dingus!")
            return

        message = self.message_database[channel]
        embed = discord.Embed(title=f"{message.author} is a sussy baka and deleted their message!", description="They really didn't want you to see that they said", color=0xFFC500)
        embed.add_field(name=f"{message.content}", value="Please make fun of them relentlessly!", inline=False)
        await ctx.respond(embed=embed)

    

def setup(bot: commands.Bot):
    bot.add_cog(Stats(bot))