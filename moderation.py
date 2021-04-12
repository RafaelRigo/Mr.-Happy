from discord.ext import commands
import discord

class Moderation(commands.Cog):
    @commands.command(
        name="kick",
        brief="A kick command",
        help="A command to kick people from the server."
    )
    @commands.has_permissions(kick_members=True)
    async def _kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "being silly! :laughing:"
        await member.kick(reason=reason)
        await ctx.send(f"{member} was kicked from the server for {reason} by {ctx.message.author}")
