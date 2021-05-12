from discord.ext import commands
import random


class Fun(commands.Cog):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def say(self, ctx, msg_to_say):
        await ctx.send(msg_to_say)

    @commands.command()
    async def rps(self, ctx, move):
        choices = ['rock', 'paper', 'scissors']
        bot = random.choice(choices).lower()
        player = move

        if player == bot:
            await ctx.send("You chose " + player +
                                       " and I chose " + bot + ".")
            await ctx.send("It's a tie! :scales:")

        elif player == 'rock':
            if bot == 'scissors':
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send('you win! :clap:')
            else:
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send(
                    "I win! :stuck_out_tongue_winking_eye:")

        elif player == "scissors":
            if bot == "paper":
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send("You win! :clap:")
            else:
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send(
                    "I win! :stuck_out_tongue_winking_eye:")

        elif player == "paper":
            if bot == "rock":
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send("You win! :clap:")
            else:
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send(
                    "I win! :stuck_out_tongue_winking_eye:")

        else:
            await ctx.send(
                "This move doesn't exist silly! :laughing:")
