import discord
import os
from dotenv import load_dotenv
from asyncio import sleep
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp

from fun import Fun
from EnglishInteractions import InteractionEnglish
from PortugueseInteractions import InteractionsPortuguese
from moderation import Moderation
from economy import Economy
# from routes.utils import app
from quart import Quart, redirect, url_for, render_template, request
from keep_alive import keep_alive

# app = Quart(__name__)

# @app.route("/")
# async def home():
#     return "I'm alive!"

load_dotenv()

TOKEN = os.getenv['TOKEN']

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
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command doesn't exist! Use $help to see what commands you can use.")
    raise error


keep_alive()


def run():
    bot.add_cog(Moderation(bot))
    bot.add_cog(Fun(bot))
    bot.add_cog(InteractionsPortuguese(bot))
    bot.add_cog(InteractionEnglish(bot))
    bot.add_cog(Economy(bot))
    bot.run(TOKEN)
    bot.loop.create_task(app.run_task('0.0.0.0'))


if __name__ == "__main__":
    run()
