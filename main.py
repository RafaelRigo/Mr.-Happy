import discord
import os
from dotenv import load_dotenv
from asyncio import sleep
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp

from fun import Fun
from moderation import Moderation
from economy import Economy
from zen import ZenQuotes
from keep_alive import keep_alive
load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(
    command_prefix="$",
    description="A friendly bot with games, cool commands and an economy system."
)

nav = DefaultMenu("◀️", "▶️", "❌")
bot.help_command = PrettyHelp(navigation=nav, color=discord.Colour.orange())


@bot.event
async def on_ready():
    print("I'm in")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f'{ctx.message.author.mention} you need to wait {error.retry_after:.2f} seconds to use this command again.')


keep_alive()


def run():
    bot.add_cog(ZenQuotes(bot))
    bot.add_cog(Moderation(bot))
    bot.add_cog(Fun(bot))
    bot.add_cog(Economy(bot))
    bot.run(TOKEN)


if __name__ == "__main__":
    run()
