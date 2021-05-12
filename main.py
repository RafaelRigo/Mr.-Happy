import discord
import os
from dotenv import load_dotenv
from discord.ext import commands as cmd

from fun import Fun
from economy import Economy
from zen import ZenQuotes
from keep_alive import keep_alive
load_dotenv()

TOKEN = os.getenv('TOKEN')


bot = cmd.Bot(
    command_prefix=['>', '~', '='],
    description="A discord bot that has zen commands, an economy system, games and moderation",
)

bot.remove_command('help')


@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title='Help', description='My prefixes are >, ~, =', color=discord.Colour.orange())
    embed.add_field(name='Economy', value='`=help economy`')
    embed.add_field(name='Fun', value='`=help fun`')
    embed.add_field(name='Zen Quotes', value='`BUGGED`')
    embed.add_field(name='Moderation', value='`Coming soon…`')

    await ctx.send(embed=embed)


@help.command()
async def economy(ctx):
    embed = discord.Embed(title='Economy', description='All the economy commands', color=discord.Colour.orange())
    embed.add_field(name='work', value='work and get some money\n**Usage:**\n`=work`')
    embed.add_field(name='money', value='check your money or another user\'s money\n**Usage:**\n`=money [@user]`')
    embed.add_field(name='pay', value='give money to other users\n**Usage:**\n`=pay <@user> <amount>`')
    
    await ctx.send(embed=embed)

@help.command()
async def fun(ctx):
    embed = discord.Embed(title='Fun', description='All the fun commands', color=discord.Colour.orange())
    embed.add_field(name='ping', value='ping pong!\n**Usage:**\n`=ping`')
    embed.add_field(name='say', value='make me say a word\n**Usage:**\n`=say <word>`')
    embed.add_field(name='rps', value='rock paper scissors\n**Usage:**\n`=rps <rock, paper or scissors>`')
    
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("I'm in")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        await ctx.send(
            f'{ctx.message.author.mention} you need to wait {error.retry_after:.2f} seconds to use this command again.')


keep_alive()


def run():
    bot.add_cog(ZenQuotes(bot))
    bot.add_cog(Fun(bot))
    bot.add_cog(Economy(bot))
    bot.run(TOKEN)


if __name__ == "__main__":
    run()
