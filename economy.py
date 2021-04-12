from discord.ext import commands
import random
import os
from easypydb import DB

dbtoken = os.environ["dbtoken"]
database = DB("EconomyDB", dbtoken)

class Economy(commands.Cog):
    '''All Economy commands'''
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command(
        name="work",
        brief="Work and get some money",
        help="Use this command to work and earn a random amount of money"
    )
    async def _work(self, ctx):
        database.load()
        money = random.randint(70, 150)
        await ctx.send(
            f"{ctx.message.author.mention} worked really hard and received {money} happy coins!"
        )
        try:
            balance = database[str(ctx.message.author.id)]
        except:
            balance = 0
        database[str(ctx.message.author.id)] = balance + money

    @commands.command(
        name="balance",
        brief="Check your balance",
        help="Get the total amount of money that is in your balance"
    )
    async def _balance(self, ctx):
        database.load()
        try:
            balance = database[str(ctx.message.author.id)]
        except:
            balance = 0
        await ctx.send(f"{ctx.message.author.mention} has {balance} happy coins!")
