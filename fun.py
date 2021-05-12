from discord.ext import commands
import random


class Fun(commands.Cog):
    '''All the fun commands'''
    @commands.command(name="ping",
                      brief="Ping Pong!",
                      help="Use this command to make me reply with Pong!")
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(name="say",
                      brief="Makes me say a word",
                      help="Use this command to make me say any word you want")
    async def say(self, ctx, msg_to_say):
        await ctx.send(msg_to_say)

    @commands.command(
        name="rps",
        brief="A rock paper scissors game",
        help=
        "Just like a normal rock paper scissors. Rock beats scissors, scissors beats paper and paper beats rock."
    )
    async def rps(self, ctx, move):
        choices = ['rock', 'paper', 'scissors']
        bot = random.choice(choices).lower()
        player = move

        if player == bot:
            await ctx.send("You chose " + player +
                                       " and I chose " + bot + ".")
            await ctx.send("It's a tie! :clap:")

        elif player == 'rock':
            if bot == 'scissors':
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send('you win! :sob:')
            else:
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send(
                    "I win! :stuck_out_tongue_winking_eye:")

        elif player == "scissors":
            if bot == "paper":
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send("You win! :sob:")
            else:
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send(
                    "I win! :stuck_out_tongue_winking_eye:")

        elif player == "paper":
            if bot == "rock":
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send("You win! :sob:")
            else:
                await ctx.send("You chose " + player +
                                           " and I chose " + bot + ".")
                await ctx.send(
                    "I win! :stuck_out_tongue_winking_eye:")

        else:
            await ctx.send(
                "This move doesn't exist silly! :laughing:")
