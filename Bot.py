import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables (BOT_TOKEN, GUILD_ID, API_URL)
load_dotenv()

# Enable intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Load all command files from /src/commands
for filename in os.listdir("./src/commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"src.commands.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

# Start bot
bot.run(os.getenv("BOT_TOKEN"))
