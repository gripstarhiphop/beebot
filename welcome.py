import discord
from sys import platform
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font

class Welcome(commands.Cog):
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
    async def on_member_join(self, member):
        if member.guild.id == 580587544287379456:
            if member.bot:
                role = discord.utils.get(member.guild.roles, name="Bots")
                if role not in member.roles:
                    await member.add_roles(role)
            # else:
            #     role = discord.utils.get(member.guild.roles, name="Member")
            
            channel = await self.bot.fetch_channel(600759570985648148)
            backdrop = Editor(f"/root/beebot/domusassets/Domus_Welcome.png")
            userpfp = await load_image_async(str(member.display_avatar))
            userpfp = Editor(userpfp).resize((250, 250)).circle_image()
            backdrop.paste(userpfp.image, (425, 60))
            font = Font("/usr/share/fonts/Poppins/Poppins-Regular.ttf", size = 50)
            smallfont = Font("/usr/share/fonts/Poppins/Poppins-Regular.ttf", size = 40)
            tinyfont = Font("/usr/share/fonts/Poppins/Poppins-Regular.ttf", size = 20)
            memberCount = member.guild.member_count
            #username
            backdrop.text(
                (300, 10), 
                f"{str(member)} just joined!", 
                font=smallfont, 
                color="white"
            )
            backdrop.text(
                (425, 460), 
                f"Member #{memberCount}", 
                font=smallfont, 
                color="black"
            )
            file = discord.File(fp=backdrop.image_bytes, filename="welcomecard.png")
            await channel.send(f"Welcome to {str(member.guild.name)} {member.mention}, enjoy your stay!", file=file)
        elif member.guild.id == 943741853239492688:
            if member.bot:
                role = discord.utils.get(member.guild.roles, name="Bots")
            else:
                role = discord.utils.get(member.guild.roles, name="Rookie")
            if role not in member.roles:
               await member.add_roles(role)
            channel = await self.bot.fetch_channel(1083094117078278234)
            backdrop = Editor(f"/root/beebot/cards/man_welcome_card2.png")
            userpfp = await load_image_async(str(member.display_avatar))
            userpfp = Editor(userpfp).resize((250, 250)).circle_image()
            backdrop.paste(userpfp.image, (425, 65))
            font = Font("/usr/share/fonts/Poppins/Poppins-Regular.ttf", size = 50)
            smallfont = Font("/usr/share/fonts/Poppins/Poppins-Regular.ttf", size = 40)
            tinyfont = Font("/usr/share/fonts/Poppins/Poppins-Regular.ttf", size = 20)
            memberCount = member.guild.member_count
            #username
            backdrop.text(
                (300, 20), 
                f"{str(member)} just joined!", 
                font=smallfont, 
                color="white"
            )
            backdrop.text(
                (425, 410), 
                f"Member #{memberCount}", 
                font=smallfont, 
                color="white"
            )
            file = discord.File(fp=backdrop.image_bytes, filename="welcomecard.png")
            await channel.send(f"Welcome to {str(member.guild.name)} {member.mention}, enjoy your stay!", file=file)



def setup(bot: commands.Bot):
    bot.add_cog(Welcome(bot))