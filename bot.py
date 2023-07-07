import time
import discord
from dotenv import load_dotenv
import os
load_dotenv()
count_message_hello = 0
bosniacy = []
def run_discord_bot():
    intentse = discord.Intents.default()
    intentse.message_content = True
    intentse.messages = True
    intentse.members = True
    intentse.typing = True
    client = discord.Client(intents=intentse)

    @client.event   
    async def on_ready():
        print(f'{client.user} in now runing!')
        await client.change_presence(activity=discord.Game("Spanie..."), status=discord.Status.dnd)

    @client.event
    async def on_message_delete(message):
        channel = client.get_channel(os.getenv('DELETED_MESSAGE_CHANEL_ID'))
        msg = f'{message.author()}:{message.author.id} Skasował wiadomość na:{message.channel()}. Która zawierała: "{message.content}"'
        if message.author.id != os.getenv('ADMIN_ID'):
         await channel.send(msg)

    @client.event
    async def on_message(message):

        hej = message.content.lower()

        if message.author == client.user:
            return

        if message.author.id in bosniacy:
            return

        if hej.startswith('hej'):
            bosniacy.append(message.author.id)
            await message.channel.send(':wave:')



    client.run(os.getenv('TOKEN'))

def bosniacy_loop():

    while True:
        czas = time.localtime()
        if czas.tm_hour == 20:
            bosniacy.clear()
        time.sleep(900)