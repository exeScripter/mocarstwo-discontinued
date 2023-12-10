# Import the required modules
import discord
import os 
from discord.ext import commands

# Import the .env
from dotenv import load_dotenv

class MocarstwoClient(discord.Client):
    async def on_ready(self):
        print("Czołem!")
        print(f'Zalogowano jako {self.user}!')

    async def on_message(self, message):
        print(f'Wiadomość od {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MocarstwoClient(intents=intents)

# Load .env
load_dotenv()
client.run(os.getenv('TOKEN'))
    