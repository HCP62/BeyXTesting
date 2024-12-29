import discord
from discord.ext import commands
import match_runner
from beyblade import Beyblade
from match import Match
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

channel_id = 1322805013818638386  # Your channel ID

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="test")
async def test(ctx):
    await ctx.send("test")

# Rest of your commands remain the same...

bot.run(TOKEN)