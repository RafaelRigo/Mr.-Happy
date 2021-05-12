from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import discord
from easypydb import DB

load_dotenv()

dbtoken = os.getenv("dbtoken")
database = DB("EconomyDB", dbtoken)


class Economy(commands.Cog):
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def work(self, ctx):
        database.load()
        money = random.randint(25, 100)
        embed = discord.Embed(title=f"{ctx.message.author}",
                              description=f"{ctx.message.author.mention} worked hard and received {money} happy coins!")
        await ctx.send(embed=embed)
        try:
            balance = database[str(ctx.message.author.id)]
        except:
            balance = 0
        database[str(ctx.message.author.id)] = balance + money

    @commands.command()
    async def money(self, ctx, member: discord.User = None):
        database.load()
        if member is None:
            try:
                balance = database[str(ctx.message.author.id)]
            except:
                balance = 0
            await ctx.send(f"{ctx.message.author.mention} you have {balance} happy coins!")
        else:
            try:
                balance = database[str(member.id)]
            except:
                balance = 0
            await ctx.send(f"{ctx.message.author.mention}\n{member.name} has {balance} happy coins!")

    @commands.command()
    async def pay(self, ctx, member: discord.User, money):
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
                f"{ctx.message.author.mention} you don't have enough happy coins to pay {money} happy coins to {member.mention}")
        else:
            database[str(member.id)] = receiverbalance + int(money)
            database[str(ctx.message.author.id)] = balance - int(money)

            embed = discord.Embed(title="The payment was a success!",
                                  description=f"{ctx.message.author.mention} your payment of {money} happy coins to {member.mention} was a success!",
                                  color=discord.Colour.orange())
            await ctx.send(embed=embed)
