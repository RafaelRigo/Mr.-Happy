from discord.ext import commands
import random


class Fun(commands.Cog):
    '''All the fun commands'''
    @commands.command(name="ping",
                      brief="Ping Pong!",
                      help="Use this command to make me reply with Pong!")
    async def _ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(name="say",
                      brief="Makes me say a word",
                      help="Use this command to make me say any word you want")
    async def _say(self, ctx, msg_to_say):
        await ctx.send(msg_to_say)

    @commands.command(
        name="spam",
        brief="A spam command",
        help=
        "Make me spam a word in a range of 1 - 100."
    )
    async def _spam(self, ctx, word, times: int):
        for i in range(times):
            await ctx.send(word)

    @commands.command(
        name="rps",
        brief="A rock paper scissors game",
        help=
        "Just like a normal rock paper scissors. Rock beats scissors, scissors beats paper and paper beats rock."
    )
    async def _rps(self, ctx, move):
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
    @commands.command(
        name="ppt",
        brief="Rock paper scissors in portuguese.",
        help="Um pedra papel tesoura normal. Pedra vence tesoura, tesoura vence papel e papel vence pedra."
    )
    async def _ppt(self, ctx, jogada):
        choices = ['pedra', 'papel', 'tesoura']
        bot = random.choice(choices).lower()
        player = jogada

        if player == bot:
            await ctx.send("Você escolheu " + player +
                                       " e eu escolhi " + bot + ".")
            await ctx.send('Deu um empate! :clap:')

        elif player == 'pedra':
            if bot == 'tesoura':
                await ctx.send("Você escolheu " + player +
                                           " e eu escolhi " + bot + ".")
                await ctx.send('Você venceu! :sob:')
            else:
                await ctx.send("Você escolheu " + player +
                                           " e eu escolhi " + bot + ".")
                await ctx.send(
                    "Eu venci! :stuck_out_tongue_winking_eye:")

        elif player == "tesoura":
            if bot == "papel":
                await ctx.send("Você escolheu " + player +
                                           " e eu escolhi " + bot + ".")
                await ctx.send("Você venceu! :sob:")
            else:
                await ctx.send("Você escolheu " + player +
                                           " e eu escolhi " + bot + ".")
                await ctx.send(
                    "Eu venci! :stuck_out_tongue_winking_eye:")

        elif player == "papel":
            if bot == "pedra":
                await ctx.send("Você escolheu " + player +
                                           " e eu escolhi " + bot + ".")
                await ctx.send("Você venceu! :sob:")
            else:
                await ctx.send("Você escolheu " + player +
                                           " e eu escolhi " + bot + ".")
                await ctx.send(
                    "Eu venci! :stuck_out_tongue_winking_eye:")

        else:
            await ctx.send(
                "Essa jogada não existe bobinho(a)! :laughing:")
