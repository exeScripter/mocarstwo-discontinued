# Import the required modules
import discord
import asyncio
import os 
from discord.ext import commands

# Import the .env
from dotenv import load_dotenv

# Load the .env
load_dotenv()

# Intents
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Turn off the default help command
bot.remove_command('help')

# Cogs
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'[+] Załadowano {filename}!')


# Event when the bot is ready
@bot.event 
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="!help"))
    print(f'Zalogowano jako {bot.user.name}!')
    await load()  # Call the load function here


# Run the bot
bot.run(os.getenv('TOKEN'))