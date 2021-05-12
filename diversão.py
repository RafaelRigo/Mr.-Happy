import discord
import random
from discord.ext import commands


class Diversao(commands.Cog):
    @commands.command()
    async def fale(self, ctx, msg_to_say):
        await ctx.send(msg_to_say)

    @commands.command()
    async def ppt(self, ctx, jogada):
        choices = ['pedra', 'papel', 'tesoura']
        bot = random.choice(choices).lower()
        player = jogada

        if player == bot:
            await ctx.send("Você escolheu " + player + " e eu escolhi " + bot +
                           ".")
            await ctx.send('Deu um empate! :scales:')

        elif player == 'pedra':
            if bot == 'tesoura':
                await ctx.send("Você escolheu " + player + " e eu escolhi " +
                               bot + ".")
                await ctx.send('Você venceu! :clap:')
            else:
                await ctx.send("Você escolheu " + player + " e eu escolhi " +
                               bot + ".")
                await ctx.send("Eu venci! :stuck_out_tongue_winking_eye:")

        elif player == "tesoura":
            if bot == "papel":
                await ctx.send("Você escolheu " + player + " e eu escolhi " +
                               bot + ".")
                await ctx.send("Você venceu! :clap:")
            else:
                await ctx.send("Você escolheu " + player + " e eu escolhi " +
                               bot + ".")
                await ctx.send("Eu venci! :stuck_out_tongue_winking_eye:")

        elif player == "papel":
            if bot == "pedra":
                await ctx.send("Você escolheu " + player + " e eu escolhi " +
                               bot + ".")
                await ctx.send("Você venceu! :clap:")
            else:
                await ctx.send("Você escolheu " + player + " e eu escolhi " +
                               bot + ".")
                await ctx.send("Eu venci! :stuck_out_tongue_winking_eye:")

        else:
            await ctx.send("Essa jogada não existe bobinho(a)! :laughing:")
