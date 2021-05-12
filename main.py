import discord
import os
from dotenv import load_dotenv
from discord.ext import commands as cmd

from fun import Fun
from economy import Economy
from zen import ZenQuotes

from diversão import Diversao
from economia import Economia

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
    embed.add_field(name='Help in portuguese', value='`=ajuda`')

    await ctx.send(embed=embed)


@help.command()
async def economy(ctx):
    embed = discord.Embed(title='Economy', description='All the economy commands', color=discord.Colour.orange())
    embed.add_field(name='work', value='work and get some money\n\n**Usage:**\n`=work`')
    embed.add_field(name='money', value='check your money or another user\'s money\n\n**Usage:**\n`=money [@user]`')
    embed.add_field(name='pay', value='give money to another user\n\n**Usage:**\n`=pay <@user> <amount>`')
    
    await ctx.send(embed=embed)

@help.command()
async def fun(ctx):
    embed = discord.Embed(title='Fun', description='All the fun commands', color=discord.Colour.orange())
    embed.add_field(name='ping', value='ping pong!\n\n**Usage:**\n`=ping`')
    embed.add_field(name='say', value='make me say a word or phrase\n\n**Usage:**\n`=say <word or "phrase">`\nphrases need to be in double quotes')
    embed.add_field(name='rps', value='rock paper scissors\n\n**Usage:**\n`=rps <rock, paper or scissors>`')
    
    await ctx.send(embed=embed)


@bot.group(invoke_without_command=True)
async def ajuda(ctx):
    embed = discord.Embed(title='Ajuda', description='Meus prefixos são >, ~, =', color=discord.Colour.orange())
    embed.add_field(name='Economia', value='`=ajuda economia`')
    embed.add_field(name='Diversão', value='`=ajuda diversao`')
    embed.add_field(name='Moderação', value='`Em breve…`')
    embed.add_field(name='Ajuda em inglês', value='`=help`')

    await ctx.send(embed=embed)

@ajuda.command()
async def economia(ctx):
    embed = discord.Embed(title='Economia', description='Todos os comandos de economia', color=discord.Colour.orange())
    embed.add_field(name='trabalhar', value='trabalhe e ganhe dinheiro\n\n**Uso:**\n`=trabalhar`')
    embed.add_field(name='dinheiro', value='olhe seu dinheiro ou o de outro usuário\n\n**Uso:**\n`=dinheiro [@usuário]`')
    embed.add_field(name='pagar', value='dê dinheiro a outro usuário\n\n**Uso:**\n`=pagar <@usuário> <quantidade>`')
    
    await ctx.send(embed=embed)

@ajuda.command()
async def diversao(ctx):
    embed = discord.Embed(title='Diversão', description='Todos os comandos de diversão', color=discord.Colour.orange())
    embed.add_field(name='fale', value='me faça falar alguma palavra ou frase\n\n**Uso:**\n`=fale <palavra ou "frase">`\nas frases tem que estar dentro de aspas duplas')
    embed.add_field(name='ppt', value='pedra papel tesoura\n\n**Uso:**\n`=ppt <pedra, papel ou tesoura>`')
    
    await ctx.send(embed=embed)
    
@bot.event
async def on_ready():
    print("I'm in")


keep_alive()


def run():
    bot.add_cog(Economia(bot))
    bot.add_cog(Diversao(bot))
    bot.add_cog(ZenQuotes(bot))
    bot.add_cog(Fun(bot))
    bot.add_cog(Economy(bot))
    bot.run(TOKEN)


if __name__ == "__main__":
    run()
