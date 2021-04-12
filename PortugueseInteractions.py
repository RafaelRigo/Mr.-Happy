from discord.ext.commands import command, Cog


class InteractionsPortuguese(Cog):
    @Cog.listener()
    async def on_message(self, message):
        msg = message.content
        oi = ["oi", "olá", "ola"]
        tchau = ["tchau", "tchauzinho"]

        # Messages in portuguese
        if str(msg).lower in oi:
            await message.channel.send('Olá!')

        if str(msg).lower == 'tudo bem?':
            await message.channel.send('Tudo')

        if str(msg).lower == 'como vai?':
            await message.channel.send('Eu vou bem')

        if str(msg).lower == 'qual é sua comida preferida?':
            await message.channel.send('Batata doce com sushi!')

        if str(msg).lower == 'o que você come?':
            await message.channel.send(
                'Eu não como, sou só um simples bot :pensive:')

        if str(msg).lower in tchau:
            await message.channel.send("Tchauzinho!")
