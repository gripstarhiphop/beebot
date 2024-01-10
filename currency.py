import asyncpg, time, random, discord, asyncio
from discord.ext import commands, tasks
from discord.commands import slash_command, Option, permissions
from discord.commands.context import ApplicationContext

guildIDs = [929594969000390696, 580587544287379456, 340253890643755009, 765005927619231774, 691147057796218905, 389113239159439361, 621423558886817820, 943741853239492688, 1040888019906994186]
currency_name = "BeeBucks"
ihchannels = [1040859151833772083, 1040859197417459763, 1040859238379040828]

class Currency(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot
        # self.check_vc.start()
        


    
    # @tasks.loop(minutes = 15)
    # async def check_vc(self):
    #     server_ids = [580587544287379456, 943741853239492688, 340253890643755009]
    #     for server in server_ids:
    #         checkserver = self.bot.get_guild(server)
    #         if not checkserver:
    #             return
    #         for voice_channel in checkserver.voice_channels:
    #             if voice_channel.name == 'Prison':
    #                 continue
    #             if voice_channel.name == 'interrogation room':
    #                 inSecret = True
    #             if voice_channel.members:
    #                 for member in voice_channel.members:
    #                     if member.voice.self_deaf or member.voice.self_mute or member.bot:
    #                         continue
    #                     db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
    #                     result = await db.fetch(f"SELECT last_message_sent FROM beelevel WHERE guild_id = '{member.guild.id}' AND user_id = '{member.id}'")
    #                     # print(f"{member.name} just got xp for being in voice in {member.guild.name}!")
    #                     if result == []:
    #                         freshuserxp = random.randrange(10,21)
    #                         sql = f"INSERT INTO beelevel(guild_id, user_id, last_message_sent, xp, lvl, coins, messages, community_nights, infractions, inhouses) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)"
    #                         await db.execute(sql, str(member.guild.id), str(member.id), time.time(), freshuserxp, 0, 0, 0, 0, 0, 0)
    #                         return
    #                     else:
    #                         if server == 580587544287379456:
    #                             channel = await self.bot.fetch_channel(600046650479738883)
    #                         elif server == 340253890643755009:
    #                             channel = await self.bot.fetch_channel(746452169137455265)
    #                         elif server == 943741853239492688:
    #                             channel = await self.bot.fetch_channel(951764009839915028)
    #                         elif inSecret == True:
    #                             channel = await self.bot.fetch_channel(961752164961755166)
    #                         await self._givexp(member, channel)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        else:
            db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
            result = await db.fetch(f"SELECT last_message_sent, messages FROM beelevel WHERE guild_id = '{message.author.guild.id}' AND user_id = '{message.author.id}'")

            if result == []:
                freshuserxp = random.randrange(10,21)
                sql = f"INSERT INTO beelevel(guild_id, user_id, last_message_sent, xp, lvl, coins, messages, community_nights, infractions, inhouses) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)"
                await db.execute(sql, str(message.author.guild.id), str(message.author.id), time.time(), freshuserxp, 0, 0, 1, 0, 0, 0)
                
                return

            else:
                newmessagetotal = result[0]['messages'] + 1
                sql = "UPDATE beelevel SET messages = $1 WHERE guild_id = $2 AND user_id = $3"
                await db.execute(sql,  newmessagetotal, str(message.guild.id), str(message.author.id))
            
                currentTime = time.time()
                if currentTime < result[0]['last_message_sent'] + 60*5:
                    return
                else:
                    await self._givexp(message.author, message.channel)





    async def _givexp(self, member, channel):
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        resultOne = await db.fetch(f"SELECT user_id, last_message_sent, xp, lvl FROM beelevel WHERE guild_id = '{member.guild.id}' AND user_id = '{member.id}'")
        xp = int(resultOne[0]['xp'])
        xpgain = random.randrange(5,11)
        xptotal = xp + xpgain
        sql = "UPDATE beelevel SET xp = $1, last_message_sent = $2 WHERE guild_id = $3 AND user_id = $4"
        await db.execute(sql, xptotal, int(time.time()), str(member.guild.id), str(member.id))
        resultTwo = await db.fetch(f"SELECT user_id, xp, lvl, coins FROM beelevel WHERE guild_id = '{member.guild.id}' AND user_id = '{member.id}'")
        userxp = resultTwo[0]['xp']
        userlvl = resultTwo[0]['lvl']
        usercoins = resultTwo[0]['coins']
        xpceil = ((userlvl + 1) * 300 + userlvl*150 + userlvl**2) if userlvl != 0 else 300
        # xpceil = 100

        if userxp >= xpceil:
        #checks to see if user is a nitro booster in Oh Look Home, then gives them more coins if they are.
            guild = self.bot.get_guild(member.guild.id)
            profit = 250
            if member.guild.id == 580587544287379456:
                boostRole = discord.utils.get(guild.roles, name="Investor")
                if boostRole in member.roles:
                    profit = 500

            sql = "UPDATE beelevel SET lvl = $1, coins = $2 WHERE guild_id = $3 AND user_id = $4"
            await db.execute(sql, userlvl + 1, usercoins + profit, str(member.guild.id), str(member.id))
            await channel.send(f"{member.mention} has reached Level {userlvl + 1} and earned {profit} {currency_name}!")
                        
            if member.guild.id == 340253890643755009:
                guild = member.guild
                if userlvl + 1 == 1:
                    role = discord.utils.get(guild.roles, name="Baybee")
                    if role is None:
                        rolecolor = int("0xFFBF00", 16)
                        await guild.create_role(name="Baybee", colour=rolecolor)
                        role = discord.utils.get(guild.roles, name="Baybee")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 5:
                    oldrole = discord.utils.get(guild.roles, name="Baybee")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Beenager")
                    if role is None:
                        rolecolor = int("0xFFBD0B", 16)
                        await guild.create_role(name="Beenager", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Beenager")
                    if role not in member.roles:
                        await member.add_roles(role)
                                        
                elif userlvl + 1 == 10:
                    oldrole = discord.utils.get(guild.roles, name="Beenager")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Worker Bee")
                    if role is None:
                        rolecolor = int("0xF9A602", 16)
                        await guild.create_role(name="Worker Bee", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Worker Bee")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 15:
                    oldrole = discord.utils.get(guild.roles, name="Worker Bee")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Drone Bee")
                    if role is None:
                        rolecolor = int("0xEB9605", 16)
                        await guild.create_role(name="Drone Bee", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Drone Bee")
                    if role not in member.roles:
                        await member.add_roles(role)
                                        
                elif userlvl + 1 == 20:
                    oldrole = discord.utils.get(guild.roles, name="Drone Bee")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Buzz Driver")
                    if role is None:
                        rolecolor = int("0xEF820D", 16)
                        await guild.create_role(name="Buzz Driver", colour=rolecolor, hoist = True)
                    role = discord.utils.get(guild.roles, name="Buzz Driver")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 25:
                    oldrole = discord.utils.get(guild.roles, name="Buzz Driver")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Buzzness Man")
                    if role is None:
                        rolecolor = int("0xDAA520", 16)
                        await guild.create_role(name="Buzznessman", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Buzznessman")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 30:
                    oldrole = discord.utils.get(guild.roles, name="Buzznessman")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Beeliever")
                    if role is None:
                        rolecolor = int("0xEF820D", 16)
                        await guild.create_role(name="Beeliever", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Beeliever")
                    if role not in member.roles:
                        await member.add_roles(role)
                                        
                elif userlvl + 1 == 40:
                    oldrole = discord.utils.get(guild.roles, name="Beeliever")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Stingaporian")
                    if role is None:
                        rolecolor = int("0xFF7417", 16)
                        await guild.create_role(name="Stingaporian", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Stingaporian")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 50:
                    oldrole = discord.utils.get(guild.roles, name="Stingaporian")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Beehadist")
                    if role is None:
                        rolecolor = int("0xFD6A02", 16)
                        await guild.create_role(name="Beehadist", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Beehadist")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 60:
                    oldrole = discord.utils.get(guild.roles, name="Beehadist")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Pollentician")
                    if role is None:
                        rolecolor = int("0xFF4500", 16)
                        await guild.create_role(name="Pollentician", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Pollentician")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 70:
                    oldrole = discord.utils.get(guild.roles, name="Pollentician")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Celebeety")
                    if role is None:
                        rolecolor = int("0xFF5349", 16)
                        await guild.create_role(name="Celebeety", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Celebeety")
                    if role not in member.roles:
                        await member.add_roles(role)
                                        
                elif userlvl + 1 == 80:
                    oldrole = discord.utils.get(guild.roles, name="Celebeety")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Beeyonce")
                    if role is None:
                        rolecolor = int("0xFF3C44", 16)
                        await guild.create_role(name="Beeyonce", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Beeyonce")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 90:
                    oldrole = discord.utils.get(guild.roles, name="Beeyonce")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Buzz Lightyear")
                    if role is None:
                        rolecolor = int("0xFF1F26", 16)
                        await guild.create_role(name="Buzz Lightyear", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Buzz Lightyear")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 100:
                    oldrole = discord.utils.get(guild.roles, name="Buzz Lightyear")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="To Infinity and Beeyond")
                    if role is None:
                        rolecolor = int("0x520003", 16)
                        await guild.create_role(name="To Infinity and Beeyond", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="To Infinity and Beeyond")
                    if role not in member.roles:
                        await member.add_roles(role)

            else:
                guild = member.guild
                if userlvl + 1 == 1:
                    role = discord.utils.get(guild.roles, name="Rookie")
                    if role is None:
                        rolecolor = int("0xf5865d", 16)
                        await guild.create_role(name="Rookie", colour=rolecolor)
                        role = discord.utils.get(guild.roles, name="Rookie")
                    if role not in member.roles:
                        await member.add_roles(role)
                elif userlvl + 1 == 5:
                    oldrole = discord.utils.get(guild.roles, name="Rookie")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Beginner")
                    if role is None:
                        rolecolor = int("0x8dd3ce", 16)
                        await guild.create_role(name="Beginner", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Beginner")
                    if role not in member.roles:
                        await member.add_roles(role)
                elif userlvl + 1 == 10:
                    oldrole = discord.utils.get(guild.roles, name="Beginner")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Novice")
                    if role is None:
                        rolecolor = int("0xd4554e", 16)
                        await guild.create_role(name="Novice", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Novice")
                    if role not in member.roles:
                        await member.add_roles(role)
                elif userlvl + 1 == 15:
                    oldrole = discord.utils.get(guild.roles, name="Novice")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Amateur")
                    if role is None:
                        rolecolor = int("0x36889a", 16)
                        await guild.create_role(name="Amateur", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Amateur")
                    if role not in member.roles:
                        await member.add_roles(role)
                elif userlvl + 1 == 20:
                    oldrole = discord.utils.get(guild.roles, name="Amateur")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Intermediate")
                    if role is None:
                        rolecolor = int("0xb098b8", 16)
                        await guild.create_role(name="Intermediate", colour=rolecolor, hoist = True)
                    role = discord.utils.get(guild.roles, name="Intermediate")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 25:
                    oldrole = discord.utils.get(guild.roles, name="Intermediate")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Proficient")
                    if role is None:
                        rolecolor = int("0xf1d883", 16)
                        await guild.create_role(name="Proficient", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Proficient")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 30:
                    oldrole = discord.utils.get(guild.roles, name="Proficient")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Experienced")
                    if role is None:
                        rolecolor = int("0x86b25c", 16)
                        await guild.create_role(name="Experienced", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Experienced")
                    if role not in member.roles:
                        await member.add_roles(role)
                                        
                elif userlvl + 1 == 40:
                    oldrole = discord.utils.get(guild.roles, name="Experienced")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Adept")
                    if role is None:
                        rolecolor = int("0xf81050", 16)
                        await guild.create_role(name="Adept", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Adept")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 50:
                    oldrole = discord.utils.get(guild.roles, name="Adept")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Advanced")
                    if role is None:
                        rolecolor = int("0xf0b888", 16)
                        await guild.create_role(name="Advanced", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Advanced")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 60:
                    oldrole = discord.utils.get(guild.roles, name="Advanced")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Professional")
                    if role is None:
                        rolecolor = int("0x7038f8", 16)
                        await guild.create_role(name="Professional", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Professional")
                    if role not in member.roles:
                        await member.add_roles(role)

                elif userlvl + 1 == 70:
                    oldrole = discord.utils.get(guild.roles, name="Professional")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Master")
                    if role is None:
                        rolecolor = int("0xc03028", 16)
                        await guild.create_role(name="Master", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Master")
                    if role not in member.roles:
                        await member.add_roles(role)
                                        
                elif userlvl + 1 == 80:
                    oldrole = discord.utils.get(guild.roles, name="Master")
                    if oldrole in member.roles:
                        await member.remove_roles(oldrole)
                    role = discord.utils.get(guild.roles, name="Expert")
                    if role is None:
                        rolecolor = int("0xf08030", 16)
                        await guild.create_role(name="Expert", colour=rolecolor, hoist = True)
                        role = discord.utils.get(guild.roles, name="Expert")
                    if role not in member.roles:
                        await member.add_roles(role)




    
            

    @slash_command(name = 'daily', description = "claim a small chunk of cash daily")
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def daily(self, ctx: ApplicationContext):
        baseClaim = 111
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')

        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        if result == []:
            await ctx.respond("You are not entered into the system, please send a message then try again.")
            return
        else:
            boostFactor = 1
            if ctx.guild.id == 580587544287379456:
                guild = self.bot.get_guild(ctx.guild.id)
                boostRole = discord.utils.get(guild.roles, name="Ambassador")
                member = await guild.fetch_member(ctx.author.id)
                if boostRole in member.roles:
                    boostFactor = 1.5
            usercoins = result[0]['coins']
            claim = round(baseClaim * boostFactor)
            deduction = random.randrange(1,11)
            total = claim - deduction
            newbal = usercoins + total
            sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, newbal, str(ctx.author.guild.id), str(ctx.author.id))
            await ctx.respond(f"You received {total} {currency_name} for your daily redemption and now have {newbal} {currency_name}!")

    @daily.error
    async def daily_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            timer = error.retry_after / 3600
            await ctx.respond(f"It's called daily for a reason retard, can you not wait {timer:.2f} hours?")


    @slash_command(name = 'rolepurchase', description = "purchase a new role for 10,000 {currency_name}")
    async def role(self, ctx: ApplicationContext, name: Option(str, "Role Name", required = True), color: Option(str, "Role Color - must be 6 character hex code.", required = False)):

        guild = ctx.guild
        
        price = 10000
        if color != None:
            price = price + 2000
        if ctx.guild.id != 1021163872167677983:
            db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
            result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
            if result == []:
                await ctx.send("You have not been registered in the system yet, please send a message then try again")
                return
            balance = result[0]['coins']
            if balance < price:
                await ctx.respond(f"You don't have enough {currency_name} to purchase this")
                return
            else:
                newBal = balance - price
                sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
                await db.execute(sql, newBal, str(ctx.author.guild.id), str(ctx.author.id))


        if color == None:
            await guild.create_role(name=name)
            newrole = discord.utils.get(ctx.guild.roles, name=name)
        else:
            hexstring = '0x' + color
            a = int(hexstring, 16)
            await guild.create_role(name=name, colour=a)
            newrole = discord.utils.get(ctx.guild.roles, name=name)
        user = ctx.author
        await user.add_roles(newrole)
        await ctx.respond("Your new custom role has been created and assigned to you")

    @slash_command(name = 'channelpurchase', description = f"purchase a new channel for 10,000 coins")
    async def channel(self, ctx: ApplicationContext):

        guild = ctx.guild
        price = 10000

        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        if result == []:
            await ctx.respond("You have not been registered in the system yet, please send a message then try again")
            return
        else:

            balance = result[0]['coins']
            if balance < price:
                await ctx.respond(f"You don't have enough {currency_name} to purchase this")
                return
            else:
                newBal = balance - price
                sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
                await db.execute(sql, newBal, str(ctx.author.guild.id), str(ctx.author.id))


            await ctx.respond("Do you want the channel to be a voice channel?  Please type yes or no")
            def check(msg):
                return (msg.author == ctx.author) and msg.channel == ctx.channel and \
                (len(msg.content) <= 32)

            try:
                msg = await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Process timed out, please try again")
                return
            if msg.content == 'exit':
                await ctx.send("Come back later if you change your mind")
                return
            elif msg.content == 'yes':
                isVoice = True
            elif msg.content == 'no':
                isVoice = False
            else:
                await ctx.send("that is not yes or no, please try again")
                return

            await ctx.send("Please enter the channel name that you desire")
            def check(msg):
                return (msg.author == ctx.author) and msg.channel == ctx.channel and \
                (len(msg.content) <= 32)

            try:
                msg = await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Process timed out, please try again")
                return
            if msg.content == 'exit':
                await ctx.send("Come back later if you change your mind")
                return
            channelName = msg.content
            if guild.id == 580587544287379456:
                category = discord.utils.get(ctx.guild.categories, name='Custom Channels')
            if isVoice == True:
                channel = await guild.create_voice_channel(name=channelName, category=category)
            else:
                channel = await guild.create_text_channel(name=channelName, category=category)
            await ctx.send("Your channel has been successfully created")



    @slash_command(name = 'transfer', description = "send money to another user")
    async def transfer(self, ctx: ApplicationContext, transfer: Option(int, "Deposit Amount", required = True, min_value = 1, max_value = 10000), member: Option(discord.Member, "Discord Member", required = True)):
        if transfer < 0:
            await ctx.respond(f"You cannot send someone negative amounts of {currency_name}, please try again")
            return
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')

        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{member.id}'")
        if result == []:
            await ctx.respond("That user doesn't exist")
            return
        result1 = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        if result1 == []:
            await ctx.respond("You are not registered in the system, please type a message then try again")
            return

        balance = result[0]['coins']
        withdraw_balance = result1[0]['coins']
        if withdraw_balance < transfer:
            await ctx.respond(f"You do not have that many {currency_name}, please try again")
            return
        
        new_balance = balance + transfer
        new_withdraw_balance = withdraw_balance - transfer
        sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
        await db.execute(sql, new_balance, str(ctx.guild.id), str(member.id))
        sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
        await db.execute(sql, new_withdraw_balance, str(ctx.guild.id), str(ctx.author.id))

        await ctx.respond(f"{member.mention} just got {transfer} {currency_name} from {ctx.author.mention} and now has {new_balance} {currency_name}!")




    @slash_command(name = 'deposit', description = "Bot owners only")
    async def deposit(self, ctx: ApplicationContext, deposit: Option(int, "Deposit Amount", required = True, min_value = 1, max_value = 10000), member: Option(discord.Member, "Discord Member", required = True)):
        
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        if ctx.author.id != 784001588816773142:
            await ctx.respond("Nice try kid")
            return

        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{member.id}'")
        if result == []:
            await ctx.respond("That user doesn't exist")
            return

        balance = result[0]['coins']
        new_balance = balance + deposit
        sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
        await db.execute(sql, new_balance, str(ctx.guild.id), str(member.id))

        await ctx.respond(f"{member.mention} just got {deposit} {currency_name} by being a kissass and now has {new_balance} {currency_name}!")

    
    @slash_command(name = 'withdraw', description = "Bot owners only")
    async def withdraw(self, ctx: ApplicationContext, withdrawal: Option(int, "Deposit Amount", required = True, min_value = 1, max_value = 10000), member: Option(discord.Member, "Discord Member", required = True)):
        
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        if ctx.author.id != 784001588816773142:
            await ctx.respond("Nice try kid")
            return

        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{member.id}'")
        if result == []:
            await ctx.respond("That user doesn't exist")
            return

        balance = result[0]['coins']
        new_balance = balance - withdrawal
        if new_balance < 0:
            new_balance = 0
            return
        sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
        await db.execute(sql, new_balance, str(ctx.guild.id), str(member.id))

        await ctx.respond(f"{member.mention} just got {withdrawal} {currency_name} yoinked from their account and now has {new_balance} {currency_name}!")


def setup(bot: commands.Bot):
    bot.add_cog(Currency(bot))