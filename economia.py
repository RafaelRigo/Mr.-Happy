from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import discord
from easypydb import DB

load_dotenv()

dbtoken = os.getenv("dbtoken")
database = DB("EconomyDB", dbtoken)


class Economia(commands.Cog):
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def trabalhar(self, ctx):
        database.load()
        money = random.randint(25, 100)
        embed = discord.Embed(title=f"{ctx.message.author}",
                              description=f"{ctx.message.author.mention} trabalhou duro e recebeu {money} happy coins!")
        await ctx.send(embed=embed)
        try:
            balance = database[str(ctx.message.author.id)]
        except:
            balance = 0
        database[str(ctx.message.author.id)] = balance + money

    @commands.command()
    async def dinheiro(self, ctx, member: discord.User = None):
        database.load()
        if member is None:
            try:
                balance = database[str(ctx.message.author.id)]
            except:
                balance = 0
            await ctx.send(f"{ctx.message.author.mention} você tem {balance} happy coins!")
        else:
            try:
                balance = database[str(member.id)]
            except:
                balance = 0
            await ctx.send(f"{ctx.message.author.mention}\n{member.name} tem {balance} happy coins!")

    @commands.command()
    async def pagar(self, ctx, member: discord.User, money):
        database.load()
        try:
            balance = database[str(ctx.message.author.id)]
        except:
            balance = 0
        try:
            receiverbalance = database[str(member.id)]
        except:
            receiverbalance = 0

        if int(money) > balance:
            await ctx.send(
                f"{ctx.message.author.mention} você não tem happy coins suficientes para pagar {money} happy coins para {member.mention}")
        else:
            database[str(member.id)] = receiverbalance + int(money)
            database[str(ctx.message.author.id)] = balance - int(money)

            embed = discord.Embed(title="O pagamento foi um sucesso!",
                                  description=f"{ctx.message.author.mention} o seu pagamento de {money} happy coins para {member.mention} foi um sucesso!",
                                  color=discord.Colour.orange())
            await ctx.send(embed=embed)