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
palavras_tristes = ["triste", "depressido", "infeliz", "bravo", "miserável", "depressivo"]

starter_encouragements = [
    "Chear up!", "Hang in there.", "You are a great person!"
]
encorajamentos_iniciais = [
    "Anima!", "Você é uma ótima pessoa!", "Olhe a natureza para relaxar um pouco"
]

if "responding" not in db.keys():
    db["responding"] = True

if "respondendo" not in db.keys():
    db["respondendo"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote



def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
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


def atualizar_encorajamentos(mensagem_encorajadora):
    if "encorajamentos" in db.keys():
        encorajamentos = db["encorajamentos"]
        encorajamentos.append(mensagem_encorajadora)
        db["encorajamentos"] = encorajamentos

def remover_encorajamento(indice):
    encorajamentos = db["encorajamentos"]
    if len(encorajamentos) > indice:
        del encorajamentos[indice]
        db["encorajamentos"] = encorajamentos


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

    if msg == '$inspire':
        quote = get_quote()
        await message.channel.send(quote)

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

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options += db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("$new encouragement"):
        encouraging_message = msg.split("$new encouragement ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added")

    if msg.startswith("$del encouragement"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del encouragement", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$list encouragements"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements[0:])

    if msg.startswith("$encouragement responding"):
        value = msg.split("$encouragement responding ", 1)[1]
        if value.lower() == 'true':
            db['responding'] = True
            await message.channel.send('Encouragement responding is on.')
        else:
            db['responding'] = False
            await message.channel.send('Encouragement responding is off.')
    
    if db["respondendo"]:
        opções = encorajamentos_iniciais
        if "encorajamentos" in db.keys():
            opções += db["encorajamentos"]
        
        if any(word in msg for word in palavras_tristes):
            await message.channel.send(random.choice(opções))
    
    if msg.startswith("$novo encorajamento"):
        mensagem_encorajadora = msg.split("$novo encorajamento ", 1)[1]
        atualizar_encorajamentos(mensagem_encorajadora)
        await message.channel.send("Novo encorajamento adicionado")

    if msg.startswith("$remover encorajamento"):
        encorajamentos = []
        if "encorajamentos" in db.keys():
            indice = int(msg.split("$remover encorajamento", 1)[1])
            remover_encorajamento(indice)
            encorajamentos = db["encorajamentos"]
        await message.channel.send(encorajamentos)

    if msg.startswith("$listar encorajamentos"):
        encorajamentos = []
        if "encorajamentos" in db.keys():
            encorajamentos = db["encorajamentos"]
        await message.channel.send(encorajamentos[0:])

    if msg.startswith("$respostas encorajadoras"):
        value = msg.split("$respostas encorajadoras ", 1)[1]
        if value.lower() == 'ativadas':
            db['respondendo'] = True
            await message.channel.send('Respostas encorajadoras estão ativadas.')
        else:
            db['respondendo'] = False
            await message.channel.send('Respostas encorajadoras estão desativadas.')

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


keep_alive()  # makes it run forever
client.run(TOKEN)  # makes the bot be online
