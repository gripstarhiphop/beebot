import discord
from sys import platform
from discord.ext import commands


class Moderation(commands.Cog):
    """
    These commands are only for people with power!  You will be scolded if you try to use them and are just some riff-raff.
    """
    def __init__(self, bot):
        self.bot = bot
        


    #simple kick funtion
    @commands.command(pass_context=True, help="kicks a ding dong from your server")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.kick_members is not True:
            await ctx.send("You do not have the permissions to run this command")
            return
        elif member.guild_permissions.kick_members:
            await ctx.send("You do not have the permissions to run this command")
            return
        else:
            message = str(f"Hey idiot, you got kicked from a server for {reason}!  If you want to rejoin, dm Gripper#2687 and he may take pity on you!")
            await member.send(message)
            await member.kick(reason = reason)
           

    #simple ban funtion
    @commands.command(pass_context=True, help="bans a retard from your server")
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.ban_members is not True:
            await ctx.send("You do not have the permissions to run this command")
            return
        elif member.guild_permissions.ban_members:
            await ctx.send("You do not have the permissions to run this command")
            return
        else:
            message = str(f"Hey idiot, you got banned from a server for {reason}!  If you want to rejoin, dm Gripper#2687 and he may take pity on you!")
            await member.send(message)
            await member.ban(reason = reason)
            


    @commands.command(pass_context=True, help="sends someone to the shadow realm")
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.manage_messages is not True:
            await ctx.send("You do not have the permissions to run this command")
            return
        if member is None:
            await ctx.send("please enter a member that you want to mute")
            return

        muterole = discord.utils.get(ctx.guild.roles, name="Bee Bot Mute")
        plebrole = discord.utils.get(ctx.guild.roles, name="Member")
        if muterole not in member.roles:
            await member.add_roles(muterole)
        if plebrole in member.roles:
            await member.remove_roles(plebrole)
        await ctx.send(f"{member} has been muted")
        message = str(f"Hey there, you have been banished to the shadow realm by a moderator for {reason}!  Please resolve this issue with them there in order to be released")
        await member.send(message)


    @commands.command(pass_context=True, help="releases someone from the shadow realm")
    async def unmute(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.manage_messages is not True:
            await ctx.send("You do not have the permissions to run this command")
            return
        if member is None:
            await ctx.send("please enter a member that you want to unmute")
            return
        else:
            guild = member.guild
        muterole = discord.utils.get(guild.roles, name="Bee Bot Mute")
        plebrole = discord.utils.get(guild.roles, name="Member")


        if plebrole not in member.roles:
            await member.add_roles(plebrole)
        if muterole in member.roles:
            await member.remove_roles(muterole)
        await ctx.send(f"{member} has been unmuted")


    #purge messages in bulk
    @commands.command(pass_context=True, help="purge messages in bulk quantity")
    async def purge(self, ctx, *, number:int=None):
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                if number is None:
                   await ctx.send("you have put in a number idiot!")
                else:
                    deleted = await ctx.message.channel.purge(limit = number)
                    await ctx.send(f'Purged {len(deleted)} messages')
            except:
                await ctx.send("I can't purge messages in this channel")
                return
        else:
            await ctx.send("You do not have the permissions to run this command")
            return


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))