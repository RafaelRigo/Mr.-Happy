import discord
import os
import requests
import json
from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']
client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


# Says when it's ready to receive messages
@client.event
async def on_ready():
    print('We are logged in as {0.user}'.format(client))


# Checks for messages
@client.event
async def on_message(message):
    # Doesn't respond to its own messages
    if message.author == client.user:
        return

    # Commands
    if message.content == '$ping':
        await message.channel.send('Pong!')

    elif message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    elif message.content.startswith("$spam 10"):
        for x in range(10):
            await message.channel.send("spam")

    elif message.content.startswith("$spam 50"):
        for x in range(50):
            await message.channel.send("spam")

    elif message.content.startswith("$spam 75"):
        for x in range(75):
            await message.channel.send("spam")

    elif message.content.startswith("$spam 100"):
        for x in range(100):
            await message.channel.send("spam")

    elif message.content.startswith("$help"):
        await message.channel.send(
            "Hi I'm Mr. Happy and my prefix is '$'! If you used this command I think you want a list of commands right?\nSo here it is:\n\n**• ping: a command that I will reply with Pong! The typical ping pong command.\n• inspire: I will reply it with a random inspirational quote.\n• spam: I will spam the word spam but you need to define a number of times to spam available numbers: 10, 50, 75, 100.**\n\nAnd I also can chat with you! Right now we have this quastions that you can ask me:\n\n**How are you?, What's your favorite food?, What do you eat?, Are you fine? and I can also answer for hello, hi and bye.**"
        )
    
    elif message.content == '$infinity':
        await message.channel.send('.infinity')

    # Messages in english
    if message.content == 'hi' or message.content == 'Hi':
        await message.channel.send('Hello!')

    elif message.content == 'hello' or message.content == 'Hello':
        await message.channel.send('Hi!')

    elif message.content == 'How are you?' or message.content == 'how are you?':
        await message.channel.send("I'm fine")

    elif message.content == "What's your favorite food?" or message.content == "what's your favorite food?":
        await message.channel.send("Sushi with sweet potato!")

    elif message.content == "What do you eat?" or message.content == "what do you eat?":
        await message.channel.send(
            "I don't eat, I'm just a simple bot :pensive:")

    elif message.content == "Are you fine?" or message.content == "are you fine?":
        await message.channel.send("Yes, I am")

    elif message.content == "Bye" or message.content == "bye":
        await message.channel.send("Good bye!")

    # Messages in portuguese
    if message.content == 'oi' or message.content == 'Oi':
        await message.channel.send('Olá!')

    elif message.content == 'olá' or message.content == 'Olá':
        await message.channel.send('Oi!')

    elif message.content == 'Tudo bem?':
        await message.channel.send('Tudo')

    elif message.content == 'Como vai?':
        await message.channel.send('Eu vou bem')

    elif message.content == 'Qual é sua comida preferida?':
        await message.channel.send('Batata doce com sushi!')

    elif message.content == 'O que você come?':
        await message.channel.send(
            'Eu não como, sou só um simples bot :pensive:')

    elif message.content == "Tchau" or message.content == "tchau":
        await message.channel.send("Tchauzinho!")


keep_alive() # makes it run forever
client.run(TOKEN) # makes the bot be online
