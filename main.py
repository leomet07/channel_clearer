import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as " + str(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$clear'):
        await message.channel.delete()
        channel = await message.guild.create_text_channel( message.channel.name)
        await channel.send("Channel cleared.")

    if message.content.startswith('$stop'):
        await client.logout()
        exit(0)
    

client.run(os.environ["token"])
