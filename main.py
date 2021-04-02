import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from replit import db


TOKEN = os.environ['TOKEN']
client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Chear up!",
    "Hang in there.",
    "You are a great person/bot!"
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def update_encouragements(encouraging_message):
    if "encouragements" in db.key():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


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
    
    msg = message.content

    # Commands
    if msg == '$ping':
        await message.channel.send('Pong!')

    elif msg == '$inspire':
        quote = get_quote()
        await message.channel.send(quote)

    elif msg.startswith("spam"):
        if str(msg[4:]).isdigit():
            msg = int(msg[5:])
        else:
            await message.channel.send("The times to spam is not numeric… Try Again")
        
        if 1 <= msg <= 100:
            for x in range(msg):
                await message.channel.send("spam")
        else:
            await message.channel.send("Number of times to spam not in range 1 - 100")

    elif msg == '$help':
        await message.channel.send(
            "Hi I'm Mr. Happy and my prefix is '$'! If you used this command I think you want a list of commands right?\nSo here it is:\n\n**• ping: a command that I will reply with Pong! The typical ping pong command.\n• inspire: I will reply it with a random inspirational quote.\n• spam: I will spam the word spam but you need to define a number of times to spam  in a range of 1 - 100.**\n\nAnd I also can chat with you! Right now we have this quastions that you can ask me:\n\n**How are you?, What's your favorite food?, What do you eat?, Are you fine? and I can also answer for hello, hi and bye.**"
        )
    
    elif msg == '$infinity':
        await message.channel.send('s.infinity')
    
    options = starter_encouragements
    if "encouragements" in db.keys():
        options = options + db["encouragements"]
    
    elif any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))
    
    elif msg.startswith("$newencouragement"):
        encouraging_message = msg.split()
    
    elif msg.startswith('$ppt'):
        choices = ['pedra', 'papel', 'tesoura']
        bot = random.choice(choices).lower()
        player = str(msg[5:])

        if player == bot:
            await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
            await message.channel.send('Deu um empate! :clap:')
        
        elif player == 'pedra':
            if bot == 'tesoura':
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send('Você venceu! :sob:')
            else:
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Eu venci! :stuck_out_tongue_winking_eye:")
        
        elif player == "tesoura":
            if bot == "papel":
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Você venceu! :sob:")
            else:
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Eu venci! :stuck_out_tongue_winking_eye:")

        elif player == "papel":
            if bot == "pedra":
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Você venceu! :sob:")
            else:
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Eu venci! :stuck_out_tongue_winking_eye:")

        else:
            await message.channel.send("Essa jogada não existe bobinho(a)! :laughing:")

    # Messages in english
    if msg == 'hi' or msg == 'Hi':
        await message.channel.send('Hello!')

    elif msg == 'hello' or msg == 'Hello':
        await message.channel.send('Hi!')

    elif msg == 'How are you?' or msg == 'how are you?':
        await message.channel.send("I'm fine")

    elif msg == "What's your favorite food?" or msg == "what's your favorite food?":
        await message.channel.send("Sushi with sweet potato!")

    elif msg == "What do you eat?" or msg == "what do you eat?":
        await message.channel.send(
            "I don't eat, I'm just a simple bot :pensive:")

    elif msg == "Are you fine?" or msg == "are you fine?":
        await message.channel.send("Yes, I am")

    elif msg == "Bye" or msg == "bye":
        await message.channel.send("Good bye!")

    # Messages in portuguese
    if msg == 'oi' or msg == 'Oi':
        await message.channel.send('Olá!')

    elif msg == 'olá' or msg == 'Olá':
        await message.channel.send('Oi!')

    elif msg == 'Tudo bem?' or msg == 'tudo bem?':
        await message.channel.send('Tudo')

    elif msg == 'Como vai?' or msg == 'como vai?':
        await message.channel.send('Eu vou bem')

    elif msg == 'Qual é sua comida preferida?' or msg == 'qual é sua comida preferida?':
        await message.channel.send('Batata doce com sushi!')

    elif msg == 'O que você come?' or msg == 'o que você come?':
        await message.channel.send(
            'Eu não como, sou só um simples bot :pensive:')

    elif msg == "Tchau" or msg == "tchau":
        await message.channel.send("Tchauzinho!")


keep_alive() # makes it run forever
client.run(TOKEN) # makes the bot be online
