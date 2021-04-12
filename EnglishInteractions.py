from discord.ext.commands import command, Cog


class InteractionEnglish(Cog):
    @Cog.listener()
    async def on_message(self, message):
        msg = message.content
        hi = ["hi", "hello"]
        bye = ["bye", "good bye"]
        if str(msg).lower() in hi:
            await message.channel.send('Hello!')

        if str(msg).lower == 'how are you?':
            await message.channel.send("I'm fine")

        if str(msg).lower == "what's your favorite food?":
            await message.channel.send("Sushi with sweet potato!")

        if str(msg).lower == "what do you eat?":
            await message.channel.send(
                "I don't eat, I'm just a simple bot :pensive:")

        if str(msg).lower == "are you fine?":
            await message.channel.send("Yes, I am")

        if str(msg).lower in bye:
            await message.channel.send("Good bye!")
