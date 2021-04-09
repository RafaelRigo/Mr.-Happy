import discord
import os
import random
from keep_alive import keep_alive
from asyncio import sleep
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp

TOKEN = os.environ['TOKEN']
bot = commands.Bot(command_prefix="$", description="A friendly bot with games, cool commands and an economy system")
nav = DefaultMenu("◀️", "▶️", "❌")
bot.help_command = PrettyHelp(navigation=nav, color=discord.Colour.orange())

@bot.event
async def on_ready():
    print("I'm in")


class Economy(commands.Cog):
    '''All Economy commands'''
    @commands.command(
    name="work",
    brief="Work and get some money",
    help="Use this command to work and earn a random amount of money"
    )
    async def _work(self, ctx):
        pass

class Client(discord.Client):
    # Says when it's ready to receive messages
    async def on_ready(self):
        print('We are logged in as', self.user)

    # Checks for messages
    async def on_message(self, message):
        # Doesn't respond to its own messages
        if message.author == self.user:
            return

        msg = message.content

        # Messages in english
        if msg == 'hi' or msg == 'Hi':
            await message.channel.send('Hello!')

        if msg == 'hello' or msg == 'Hello':
            await message.channel.send('Hi!')

        if msg == 'How are you?' or msg == 'how are you?':
            await message.channel.send("I'm fine")

        if msg == "What's your favorite food?" or msg == "what's your favorite food?":
            await message.channel.send("Sushi with sweet potato!")

        if msg == "What do you eat?" or msg == "what do you eat?":
            await message.channel.send(
                "I don't eat, I'm just a simple bot :pensive:")

        if msg == "Are you fine?" or msg == "are you fine?":
            await message.channel.send("Yes, I am")

        if msg == "Bye" or msg == "bye":
            await message.channel.send("Good bye!")

        # Messages in portuguese
        if msg == 'oi' or msg == 'Oi':
            await message.channel.send('Olá!')

        if msg == 'olá' or msg == 'Olá':
            await message.channel.send('Oi!')

        if msg == 'Tudo bem?' or msg == 'tudo bem?':
            await message.channel.send('Tudo')

        if msg == 'Como vai?' or msg == 'como vai?':
            await message.channel.send('Eu vou bem')

        if msg == 'Qual é sua comida preferida?' or msg == 'qual é sua comida preferida?':
            await message.channel.send('Batata doce com sushi!')

        if msg == 'O que você come?' or msg == 'o que você come?':
            await message.channel.send(
                'Eu não como, sou só um simples bot :pensive:')

        if msg == "Tchau" or msg == "tchau":
            await message.channel.send("Tchauzinho!")

class Commands(discord.Client):
    async def on_ready(self):
        print("commands are ready")
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        msg = message.content

        # Commands
        if msg == '$ping':
            await message.channel.send('Pong!')

        if msg.startswith("$spam"):
            if str(msg[6:]).isdigit():
                msg = int(msg.split("$spam", 1)[1])
            else:
                await message.channel.send(
                    "The times to spam is not numeric… Try Again")

            if 1 <= msg <= 100:
                for x in range(msg):
                    await message.channel.send("spam")
            else:
                await message.channel.send(
                    "Number of times to spam not in range 1 - 100")

        if msg == '$infinity':
            await message.channel.send('s.infinity')

        if msg.startswith('$ppt'):
            choices = ['pedra', 'papel', 'tesoura']
            bot = random.choice(choices).lower()
            player = str(msg[5:])

            if player == bot:
                await message.channel.send("Você escolheu " + player +
                                        " e eu escolhi " + bot + ".")
                await message.channel.send('Deu um empate! :clap:')

            elif player == 'pedra':
                if bot == 'tesoura':
                    await message.channel.send("Você escolheu " + player +
                                            " e eu escolhi " + bot + ".")
                    await message.channel.send('Você venceu! :sob:')
                else:
                    await message.channel.send("Você escolheu " + player +
                                            " e eu escolhi " + bot + ".")
                    await message.channel.send(
                        "Eu venci! :stuck_out_tongue_winking_eye:")

            elif player == "tesoura":
                if bot == "papel":
                    await message.channel.send("Você escolheu " + player +
                                            " e eu escolhi " + bot + ".")
                    await message.channel.send("Você venceu! :sob:")
                else:
                    await message.channel.send("Você escolheu " + player +
                                            " e eu escolhi " + bot + ".")
                    await message.channel.send(
                        "Eu venci! :stuck_out_tongue_winking_eye:")

            elif player == "papel":
                if bot == "pedra":
                    await message.channel.send("Você escolheu " + player +
                                            " e eu escolhi " + bot + ".")
                    await message.channel.send("Você venceu! :sob:")
                else:
                    await message.channel.send("Você escolheu " + player +
                                            " e eu escolhi " + bot + ".")
                    await message.channel.send(
                        "Eu venci! :stuck_out_tongue_winking_eye:")

            else:
                await message.channel.send(
                    "Essa jogada não existe bobinho(a)! :laughing:")

        if msg.startswith('$rps'):
            choices = ['rock', 'paper', 'scissors']
            bot = random.choice(choices).lower()
            player = str(msg[5:])

            if player == bot:
                await message.channel.send("You chose " + player +
                                        " and I chose " + bot + ".")
                await message.channel.send("It's a tie! :clap:")

            elif player == 'rock':
                if bot == 'scissors':
                    await message.channel.send("You chose " + player +
                                        " and I chose " + bot + ".")
                    await message.channel.send('you win! :sob:')
                else:
                    await message.channel.send("You chose " + player +
                                        " and I chose " + bot + ".")
                    await message.channel.send(
                        "I win! :stuck_out_tongue_winking_eye:")

            elif player == "scissors":
                if bot == "paper":
                    await message.channel.send("You chose " + player +
                                        " and I chose " + bot + ".")
                    await message.channel.send("You win! :sob:")
                else:
                    await message.channel.send("You chose " + player +
                                        " and I chose " + bot + ".")
                    await message.channel.send(
                        "I win! :stuck_out_tongue_winking_eye:")

            elif player == "paper":
                if bot == "rock":
                    await message.channel.send("You chose " + player +
                                        " and I chose " + bot + ".")
                    await message.channel.send("You win! :sob:")
                else:
                    await message.channel.send("You chose " + player +
                                        " and I chose " + bot + ".")
                    await message.channel.send(
                        "I win! :stuck_out_tongue_winking_eye:")

            else:
                await message.channel.send(
                    "This move doesn't exist silly! :laughing:")

        if msg.startswith("$say"):
            msg = str(msg[5:])
            await message.channel.send(msg)


keep_alive()  # makes it run forever
client = Client()
client.run(TOKEN)  # makes the bot be online
commands = Commands()
commands.run(TOKEN)

def run():
    bot.run(TOKEN)

if __name__ == "__main__":
    run()
