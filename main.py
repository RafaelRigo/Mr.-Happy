import discord
import os
from keep_alive import keep_alive
from asyncio import sleep
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp
from economy import Economy
from fun import Fun
from EnglishInteractions import InteractionEnglish
from PortugueseInteractions import InteractionsPortuguese
from moderation import Moderation

TOKEN = os.environ['TOKEN']

bot = commands.Bot(
    command_prefix="$",
    description="A friendly bot with games, cool commands and an economy system."
)

nav = DefaultMenu("◀️", "▶️", "❌")
bot.help_command = PrettyHelp(navigation=nav, color=discord.Colour.orange())


@bot.event
async def on_ready():
    print("I'm in")


keep_alive()  # makes it run forever


def run():
    bot.add_cog(Moderation(bot))
    bot.add_cog(Fun(bot))
    bot.add_cog(InteractionsPortuguese(bot))
    bot.add_cog(InteractionEnglish(bot))
    bot.add_cog(Economy(bot))
    bot.run(TOKEN)


if __name__ == "__main__":
    run()
