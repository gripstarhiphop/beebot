import discord
from sys import platform
from discord.ext import commands
from discord.ui import Button


roleids = [864057703683719198]


# class MyView(discord.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)
#     @discord.ui.button(label="Inhouse Ping", custom_id="pingbtn", style=discord.ButtonStyle.green, emoji='<:Ping:864802541899218964>')
#     async def pingcb(self, button, interaction):
#         await interaction.respond.send_message("ping", ephemeral=True)


class ReactRoles(commands.Cog):
    """
    your mom doesn't love you
    """
    def __init__(self, bot):
        self.bot = bot
        if platform.startswith("lin"):
            self.path = "/root/beebot/hadesgifs/"
        else:
            self.path = "./media/"


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

       olhembedID = 971264800820703312
       bdsmgameembedID = 941273636155846727
       bdsmotherembedID = 941273637443493948
       manID = 1021345287379357746
       inhouseID = 964004308238602262
       verifyID = 971843885137559583

       if olhembedID == payload.message_id:
           member = payload.member
           guild = member.guild

           emoji = payload.emoji.name
           if emoji == '🎁':
               role = discord.utils.get(guild.roles, name="Giveaways")
           elif emoji == '🎨':
               role = discord.utils.get(guild.roles, name="Artist")
           elif emoji == 'AYAYA':
               role = discord.utils.get(guild.roles, name="Anime")
           elif emoji == '🎦':
               role = discord.utils.get(guild.roles, name="Events")
           elif emoji == '🏆':
              role = discord.utils.get(guild.roles, name="Tournaments")
           elif emoji == '🏅':
              role = discord.utils.get(guild.roles, name="Contests")
           elif emoji == 'League':
              role = discord.utils.get(guild.roles, name="League Of Legends")
           elif emoji == 'Minecraft':
               role = discord.utils.get(guild.roles, name="Minecraft")
           elif emoji == 'Valorant':
               role = discord.utils.get(guild.roles, name="Valorant")
           elif emoji == 'Apex':
               role = discord.utils.get(guild.roles, name="Apex Legends")
           elif emoji == 'Rocket':
               role = discord.utils.get(guild.roles, name="Rocket League")
           elif emoji == 'Fortnite':
               role = discord.utils.get(guild.roles, name="Fortnite")
           elif emoji == 'Meatballs':
               role = discord.utils.get(guild.roles, name="DST")
           

           if role not in member.roles:
               await member.add_roles(role)

       elif bdsmgameembedID == payload.message_id:
           member = payload.member
           guild = member.guild
           emoji = payload.emoji.name
           if emoji == 'League':
               role = discord.utils.get(guild.roles, name = "League of Legends")
           elif emoji == 'Valorant':
               role = discord.utils.get(guild.roles, name = "Valorant")
           elif emoji == 'pikawah':
               role = discord.utils.get(guild.roles, name = "Scary Games")
           elif emoji == 'block':
               role = discord.utils.get(guild.roles, name = "Tetris")
           elif emoji == '🧩':
               role = discord.utils.get(guild.roles, name = "Puzzles")
           elif emoji == 'Rocket':
               role = discord.utils.get(guild.roles, name = "Rocket League")
           elif emoji == 'peepoparty':
               role = discord.utils.get(guild.roles, name = "Party Games")
           elif emoji == '🍻':
               role = discord.utils.get(guild.roles, name = "DRUNK Party Games")
           

           if role not in member.roles:
               await member.add_roles(role)
        
       elif bdsmotherembedID == payload.message_id:
           member = payload.member
           guild = member.guild
           emoji = payload.emoji.name
           if emoji == '🎥':
               role = discord.utils.get(guild.roles, name = "Movie Night")
           elif emoji == 'feelsanimeman':
               role = discord.utils.get(guild.roles, name = "Anime")
           elif emoji == '⛪':
               role = discord.utils.get(guild.roles, name = "Sunday Bible Study")
           elif emoji == 'peepobirthday':
               role = discord.utils.get(guild.roles, name = "Birthday")
           elif emoji == 'peepopumpkin':
               role = discord.utils.get(guild.roles, name = "AHS Night")
           elif emoji == 'peepers':
               role = discord.utils.get(guild.roles, name = "Where The Goons At?")

           if role not in member.roles:
               await member.add_roles(role)

       elif inhouseID == payload.message_id:
           member = payload.member
           guild = member.guild
           emoji = payload.emoji.name
           if emoji ==  'Ping':
               role = discord.utils.get(guild.roles, name = "Inhouse Ping")
           if role not in member.roles:
               await member.add_roles(role)


       elif verifyID == payload.message_id:

           guild = self.bot.get_guild(payload.guild_id)
           member = await guild.fetch_member(payload.user_id) 

           emoji = payload.emoji.name
           if emoji == '☑️':
               role = discord.utils.get(guild.roles, name = "Member")
           if role not in member.roles:
               await member.add_roles(role)
        
       elif manID == payload.message_id:
           guild = self.bot.get_guild(payload.guild_id)
           member = await guild.fetch_member(payload.user_id)

           emoji = payload.emoji.name

           if emoji == '🥳':
               role = discord.utils.get(guild.roles, name = "Party Games")
           elif emoji == 'poker':
               role = discord.utils.get(guild.roles, name = "Poker Night")
           elif emoji == 'observing':
               role = discord.utils.get(guild.roles, name = "Observing")
           elif emoji == '🎮':
               role = discord.utils.get(guild.roles, name = "Gaming")
           elif emoji == 'clueless':
               role = discord.utils.get(guild.roles, name = "League of Legends addict")
           elif emoji == 'god':
               role = discord.utils.get(guild.roles, name = "Fortnite") 
           elif emoji == 'nathansyndrome':
               role = discord.utils.get(guild.roles, name = "pedophile")
           elif emoji == 'meow':
               role = discord.utils.get(guild.roles, name = "w*man")
           elif emoji == '👶':
               role = discord.utils.get(guild.roles, name = "Balls Reveal Soon!")
           elif emoji == 'jugg':
               role = discord.utils.get(guild.roles, name = "Snow Mexican") 

           if role not in member.roles:
               await member.add_roles(role) 



    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        olhembedID = 964497702706626590
        bdsmgameembedID = 941273636155846727
        bdsmotherembedID = 941273637443493948
        inhouseID = 964004308238602262
        manID = 1021345287379357746
        
        if olhembedID == payload.message_id:

            guild = self.bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)

            emoji = payload.emoji.name
            if emoji == '🎁':
                role = discord.utils.get(guild.roles, name="Giveaways")
            elif emoji == '🎨':
                role = discord.utils.get(guild.roles, name="Artist")
            elif emoji == 'AYAYA':
                role = discord.utils.get(guild.roles, name="Anime")
            elif emoji == '🎦':
                role = discord.utils.get(guild.roles, name="Events")
            elif emoji == '🏆':
               role = discord.utils.get(guild.roles, name="Tournaments")
            elif emoji == 'League':
               role = discord.utils.get(guild.roles, name="League Of Legends")
            elif emoji == 'Minecraft':
                role = discord.utils.get(guild.roles, name="Minecraft")
            elif emoji == 'Valorant':
                role = discord.utils.get(guild.roles, name="Valorant")
            elif emoji == 'Apex':
                role = discord.utils.get(guild.roles, name="Apex Legends")
            elif emoji == 'Rocket':
                role = discord.utils.get(guild.roles, name="Rocket League")
            elif emoji == 'Fortnite':
                role = discord.utils.get(guild.roles, name="Fortnite")
            elif emoji == 'Meatballs':
                role = discord.utils.get(guild.roles, name="DST")
            elif emoji == 'Runeterra':
                role = discord.utils.get(guild.roles, name="Legends of Runeterra")

            if member is not None:
                if role in member.roles:
                    await member.remove_roles(role)

        elif bdsmgameembedID == payload.message_id:

           guild = self.bot.get_guild(payload.guild_id)
           member = await guild.fetch_member(payload.user_id) 

           emoji = payload.emoji.name
           if emoji == 'League':
               role = discord.utils.get(guild.roles, name = "League of Legends")
           elif emoji == 'Valorant':
               role = discord.utils.get(guild.roles, name = "Valorant")
           elif emoji == 'pikawah':
               role = discord.utils.get(guild.roles, name = "Scary Games")
           elif emoji == 'block':
               role = discord.utils.get(guild.roles, name = "Tetris")
           elif emoji == '🧩':
               role = discord.utils.get(guild.roles, name = "Puzzles")
           elif emoji == 'Rocket':
               role = discord.utils.get(guild.roles, name = "Rocket League")
           elif emoji == 'peepoparty':
               role = discord.utils.get(guild.roles, name = "Party Games")
           elif emoji == '🍻':
               role = discord.utils.get(guild.roles, name = "DRUNK Party Games")

           if member is not None:
                if role in member.roles:
                    await member.remove_roles(role)


        elif bdsmotherembedID == payload.message_id:

           guild = self.client.get_guild(payload.guild_id)
           member = await guild.fetch_member(payload.user_id) 

           emoji = payload.emoji.name
           if emoji == '🎥':
               role = discord.utils.get(guild.roles, name = "Movie Night")
           elif emoji == 'feelsanimeman':
               role = discord.utils.get(guild.roles, name = "Anime")
           elif emoji == '⛪':
               role = discord.utils.get(guild.roles, name = "Sunday Bible Study")
           elif emoji == 'peepobirthday':
               role = discord.utils.get(guild.roles, name = "Birthday")
           elif emoji == 'peepopumpkin':
               role = discord.utils.get(guild.roles, name = "AHS Night")
           elif emoji == 'peepers':
               role = discord.utils.get(guild.roles, name = "Where The Goons At?")

           if member is not None:
                if role in member.roles:
                    await member.remove_roles(role)


        elif inhouseID == payload.message_id:
           guild = self.bot.get_guild(payload.guild_id)
           member = await guild.fetch_member(payload.user_id)

           emoji = payload.emoji.name 
           if emoji ==  'Ping':
               role = discord.utils.get(guild.roles, name = "Inhouse Ping")
           if role in member.roles:
               await member.remove_roles(role)

        
        elif manID == payload.message_id:
           guild = self.bot.get_guild(payload.guild_id)
           member = await guild.fetch_member(payload.user_id) 

           emoji = payload.emoji.name

           if emoji == '🥳':
               role = discord.utils.get(guild.roles, name = "Party Games")
           elif emoji == 'poker':
               role = discord.utils.get(guild.roles, name = "Poker Night")
           elif emoji == 'observing':
               role = discord.utils.get(guild.roles, name = "Observing")
           elif emoji == '🎮':
               role = discord.utils.get(guild.roles, name = "Gaming")
           elif emoji == 'clueless':
               role = discord.utils.get(guild.roles, name = "League of Legends addict")
           elif emoji == 'god':
               role = discord.utils.get(guild.roles, name = "Fortnite") 
           elif emoji == 'nathansyndrome':
               role = discord.utils.get(guild.roles, name = "pedophile")
           elif emoji == 'meow':
               role = discord.utils.get(guild.roles, name = "w*man")
           elif emoji == '👶':
               role = discord.utils.get(guild.roles, name = "Balls Reveal Soon!")
           elif emoji == 'jugg':
               role = discord.utils.get(guild.roles, name = "Snow Mexican") 

           if member is not None:
                if role in member.roles:
                    await member.remove_roles(role) 

       


    #handles embed for Oh Look Home React Roles
    @commands.command(pass_context=True, help="Gripper only")
    @commands.is_owner()
    async def roleembed(self, ctx):
       embed0 = discord.Embed(color=0xFFC500)
       embed0.set_image(url='https://cdn.discordapp.com/attachments/722963834398179413/971209789663244379/Domus_Roles.png')
       msg = await ctx.send(embed=embed0)

       embed1 = discord.Embed(title="**Domus Server Rank Roles**", description="**These are the roles that are awarded to users based on their staff or experience server rank**", color=0xFFC500)
       embed1.add_field(name="__**Staff Roles**__", value="<@&747276941756989571>**: Administrator**\n <@&581324523148673038>**: Moderator**\n <@&910775027681591296>**: Inhouse Staff**", inline=False)
       embed1.add_field(name="__**Server Ranks**__", value="<@&641577751517724672>**: Nitro Boosters**\n <@&963724588582309920>**: Level 80**\n <@&963724768576692225>**: Level 70**\n <@&963724439390945281>**: Level 60**\n <@&963724306964168734>**: Level 50**\n <@&963724055272378428>**: Level 40**\n <@&963723868437106719>**: Level 30**\n <@&963723679466917938>**: Level 25**\n <@&963723498386243675>**: Level 20**\n <@&963723166981713921>**: Level 15**\n  <@&963723019790979093>**: Level 10**\n  <@&963722858012483614>**: Level 5**\n  <@&963722685295255603>**: Level 1**\n\n **Members who Nitro Boost the server will also get custom role their choice as a thank you.**", inline=False)
       msg = await ctx.send(embed=embed1)
       
       embed = discord.Embed(title="**Domus React Roles**", description="**React to this message with the corresponding emojis to receive the roles that you desire**", color=0xFFC500)
       embed.add_field(name="__**Roles**__", value="**Giveaways:**\U0001F381 \n **Artist:**\U0001F3A8 \n **Anime:**<:AYAYA:764719193722585089> \n **Events:**🎦 \n **Tournaments:**\U0001F3C6", inline=False)
       embed.add_field(name="__**Games**__", value="**League of Legends:**<:League:690334779492794439> \n **Minecraft:**<:Minecraft:690336288645447902> \n **Valorant:**<:Valorant:869348121128357968> \n **Apex Legends:**<:Apex:905931192560394290> \n **Fortnite:**<:Fortnite:905932551594602506>", inline=False)
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/722963834398179413/971209789663244379/Domus_Roles.png")

       msg = await ctx.send(embed=embed)
       await msg.add_reaction('🎁')
       await msg.add_reaction('🎨')
       await msg.add_reaction('<:AYAYA:764719193722585089>')
       await msg.add_reaction('🎦')
       await msg.add_reaction('🏆')
       await msg.add_reaction('<:League:690334779492794439>')
       await msg.add_reaction('<:Minecraft:690336288645447902>')
       await msg.add_reaction('<:Valorant:869348121128357968>')
       await msg.add_reaction('<:Apex:905931192560394290>')
       await msg.add_reaction('<:Fortnite:905932551594602506>')


    @commands.command(pass_context=True, help="Gripper only")
    @commands.is_owner()
    async def ruleembed(self, ctx):
       embed0 = discord.Embed(color=0xFFC500)
       embed0.set_image(url='https://cdn.discordapp.com/attachments/722963834398179413/971209790221062164/Domus_Rules.png')
       msg = await ctx.send(embed=embed0)

       embed = discord.Embed(title="**Domus Server Rules**", description="**Rules in this server will be enforced in a three strikes method.  Based upon the severity of the offense, punishments will be dealt out at the discretion of our staff.  Warnings will be given at first, then mutes, then a kick or a ban.**", color=0xFFC500)
       embed.add_field(name="**Rule #1**", value = "No homophobic or racial slurs whatsoever. Harrassment and discrimination are not welcome.", inline=False)
       embed.add_field(name="**Rule #2**", value = "Banter between members is permitted, but all serious drama must go in DMs. \n", inline=False)
       embed.add_field(name="**Rule #3**", value = "No NSFW content whatsoever.  Keep in mind that there are many other people in the server.  Please be considerate of them. \n", inline=False)
       embed.add_field(name="**Rule #4**", value = "No spamming.  Intentionally clogging up channels is annoying and spams people with notifications. \n", inline=False)
       embed.add_field(name="**Rule #5**", value = "Use each channel for their intended purpose. \n", inline=False)
       embed.add_field(name="**Violating rules 1, 2, and 3 will receive (Warning/1 Hour Mute/1 Day Mute/Kick) as punishments.  We will be more lenient with Rules 4 and 5 as they are not as serious.**", value = "\n**The <@&581324523148673038> will have the final say in all situations, even if it is not listed above.  Do not try to bend the rules.**")

       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/722963834398179413/971209790221062164/Domus_Rules.png")

       msg = await ctx.send(embed=embed)

    @commands.command(pass_context=True, help="Gripper only")
    @commands.is_owner()
    async def applyembed(self, ctx):
       embed0 = discord.Embed(color=0xFFC500)
       embed0.set_image(url='https://cdn.discordapp.com/attachments/722963834398179413/971209790552432710/Domus_Staff.png')
       msg = await ctx.send(embed=embed0)

       embed = discord.Embed(title="**Domus Staff Application**", description="If you would like to become a member of the moderator team or the inhouse staff and help us manage the server, please fill out this application below!  Your application as well as your history in the community will be the key deciding factors that determine whether we accept or reject you. \nhttps://docs.google.com/forms/d/e/1FAIpQLSfIreQahRB9J1VGp0zJK87a8Z9qxxVXtU0zj84Zd8VBmlooHg/viewform?usp=sf_link")
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/722963834398179413/971209790552432710/Domus_Staff.png")

       msg = await ctx.send(embed=embed)





    @commands.command(pass_context=True, help = "Gripper only")
    @commands.is_owner()
    async def bdsmembed(self, ctx):
        embed = discord.Embed(title="BDSM React Roles", description="**__Get Notified for Gamer Hours__**", color=0xFFC500)
        embed.add_field(name = "**GAME ROLES**", value = "<:League:690334779492794439> <@&941246830061191268> mostly for ARAM Inhouses \n\n<:Valorant:869348121128357968> <@&941259252146778143>\n\n<:pikawah:881773743658115123> <@&941260862277173269> dbd, devour, games that make you go AAAAH\n\n<:block:941258028173393960> <@&941250453419741204> FORECLOSURE... and sometimes Tricky Towers\n\n🧩 <@&941250582142922763> quiet puzzling hours on Tabletop Simulator\n\n<:Rocket:905925003810340894> <@&941250682302910504> we are still looking for players for our team, Dykes on Tykes. Tryouts are held every Tuesdays and Thursdays!\n\n<:peepoparty:941260045377740820> <@&941250770995646474> Fartic Phone, Codenames, Jackbox, Just Act Natural, Secret Hitler, etc. big group activities\n\n🍻 <@&941250861508743268> Same as above but more wild. 21+")
        embed0 = discord.Embed(title="BDSM React Roles", description="**__Get Notified for Other Hours__**", color=0xFFC500)
        embed0.add_field(name = "**NON-GAME RELATED ROLES**", value= "🎥 <@&663839111366443008>\n\n<:feelsanimeman:941262869339701288> <@&941251013841666100>\n\n⛪ <@&941251085220327464> big homie comes first on this holy day\n\n<:peepobirthday:941262336294023249> <@&941251177058816070> for when you'd like the whole server to celebrate your special day! You will also be notified of other people's birthdays too\n\n<:peepopumpkin:941262783029342228> <@&941251263725723668> American Horror Story streamed every October\n\n<:peepers:941262956669313054> <@&941251345451737118> For the lonely homies in this server who want to be ping abused 3-5 times a day")
        msg = await ctx.send(embed=embed)
        msg0 = await ctx.send(embed=embed0)
        await msg.add_reaction('<:League:690334779492794439>')
        await msg.add_reaction('<:Valorant:869348121128357968>')
        await msg.add_reaction('<:pikawah:881773743658115123>')
        await msg.add_reaction('<:block:941258028173393960>')
        await msg.add_reaction('🧩')
        await msg.add_reaction('<:Rocket:905925003810340894>')
        await msg.add_reaction('<:peepoparty:941260045377740820>')
        await msg.add_reaction('🍻')
        await msg0.add_reaction('🎥')
        await msg0.add_reaction('<:feelsanimeman:941262869339701288>')
        await msg0.add_reaction('⛪')
        await msg0.add_reaction('<:peepobirthday:941262336294023249>')
        await msg0.add_reaction('<:peepopumpkin:941262783029342228>')
        await msg0.add_reaction('<:peepers:941262956669313054>')




    # @commands.Cog.listener
    # async def on_ready(self):
    #     self.add_view(MyView())

    
    @commands.command(pass_context=True, help = "Gripper only")
    @commands.is_owner()
    async def house(self, ctx):
        embed = discord.Embed(title="**INHOUSE RULES\n\nRule 1 - General Rules**", description="Follow the server rules. No slurs, no NSFW, no spamming, and while banter is allowed take fights to DM's if the situation escalates.", color=0xFFC500)
        embed0 = discord.Embed(title="**Inhouse Access**", description="React with <:Ping:864802541899218964> to pinged for inhouses.", color=0xFFC500)
        embed1 = discord.Embed(title="**Rule 2 - Listen to the Captain**", description="Team Captains are decided through the Inhouse Ladder. The two highest players on the ladder who are participating in the lobby will be team captains. The lower of the two will get side selection. The role of the Team Captain is to draft their teammates through the player draft and assign the roles of the team. To help with this process, their will be a hyperlink to view all the players during the draft phase. Team Captains can determine the role a player goes to, but not the champion that they play. This is to ensure that everyone can have fun, and not be forced on Malphite/Lulu duty. Players must listen to their Team Captains for bans and roles.", color=0xFFC500)
        embed2 = discord.Embed(title="**Rule 3 - Pausing the Game**", description="Both teams are allotted 5 minutes of pause time during games. Things can happen and players may need to pause, but the whole lobby shouldn't have to wait half an hour. When the team that requested the pause wants to unpause, they need to wait for the enemy team to say that they are ready. When both captains indicate that they're ready, the match can be unpaused.", color=0xFFC500)
        embed3 = discord.Embed(title="**Rule 4 - Unconventional Picks**", description="New technology is cool but picking something that is considered wildly off meta must be discussed with the team before hand. The entire team must unanimously approve of the pick. Locking in something that is considered troll and contributes to a loss will result in punishment.(Example of Some Unconventional Picks: Janna Top with Smite, Rakan Mid, Heimerdinger Support)", color=0xFFC500)
        embed4 = discord.Embed(title="**Rule 5 - Punishments for Griefing/AFKing/Dodging**", description="These are the most serious offenses. Having a bad game is NOT a punishable offense, however purposefully making the game hard to play for your team is. To file a report for griefing, DM the host of the lobby and the Inhouse Staff will look into it. AFKing and Dodging during draft causes inconvenience for nine other people, and will result in punishment. If a player is AFK with no signs of return, then the remaining players can exit the game and remake the lobby. The Inhouse Staff will keep records of each offense, and for each additional offense the punishments will be more severe.\nPunishments will follow this system:\n1st Offense: Warning\n2nd Offense: 1D Inhouse Ban\n3rd Offense: 1W Inhouse Ban\nNote: These act as guidelines and do not have to be followed in more extreme scenarios.", color=0xFFC500)
        embed5 = discord.Embed(title="**Rule 6 - Joining Team VCs**", description="It is required that the participating members of the team join their respective team voice channels before the start of the game. Team Voice Channels can be found below the Inhouse Channels.", color=0xFFC500)
        
        msg = await ctx.send(embed=embed)
        msg1 = await ctx.send(embed=embed1)
        msg2 = await ctx.send(embed=embed2)
        msg3 = await ctx.send(embed=embed3)
        msg4 = await ctx.send(embed=embed4)
        msg5 = await ctx.send(embed=embed5)
        msg0 = await ctx.send(embed=embed0)

        await msg0.add_reaction('<:Ping:864802541899218964>')

        
            


       

    
    @commands.command(pass_context=True, help = "Gripper only")
    @commands.is_owner()
    async def verify(self, ctx):
        embed = discord.Embed(title="**USER VERIFICATION**", description="Please react to this message with ☑️ to gain access to the rest of the server.", color=0xFFC500)
        embed.set_thumbnail(url = ctx.guild.icon.url)
        msg = await ctx.send(embed=embed)

        await msg.add_reaction('☑️')



    @commands.command(pass_context=True, help="Gripper only")
    @commands.is_owner()
    async def manembed(self, ctx):

       
       embed = discord.Embed(title="**REACT ROLES**", description="**React to this message to get epic roles for fun stuff we do**", color=0xFFC500)
       embed.add_field(name="__**Roles**__", value="**Party Games:**🥳 \n**Poker:**<:poker:1021338166264872960> \n **Watching Stuff:**<:observing:990912981904805938> \n **General Gaming:🎮**", inline=False)
       embed.add_field(name="__**Games**__", value="**League of Legends:**<:clueless:959018537484169236> \n **Fortnite:**<:god:978549016247824404> \n **osu!:**<:nathansyndrome:1007739892996001793>", inline=False)
       embed.add_field(name="__**Other**__", value="**Woman:**<:meow:1008946329290018886> \n**Underage:**👶 \n**Canadian:**<:jugg:1021342708972916776>", inline=False)
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929594997790101515/1021336156740276305/CB1A2CFE-C255-4729-A936-0DD1DF2F4E02-1.jpg")

       msg = await ctx.send(embed=embed)
       await msg.add_reaction('🥳')
       await msg.add_reaction('<:poker:1021338166264872960>')
       await msg.add_reaction('<:observing:990912981904805938>')
       await msg.add_reaction('🎮')
       await msg.add_reaction('<:clueless:959018537484169236>')
       await msg.add_reaction('<:god:978549016247824404>')
       await msg.add_reaction('<:nathansyndrome:1007739892996001793>')
       await msg.add_reaction('<:meow:1008946329290018886>')
       await msg.add_reaction('👶')
       await msg.add_reaction('<:jugg:1021342708972916776>')


def setup(bot: commands.Bot):
    bot.add_cog(ReactRoles(bot))