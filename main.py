import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables (BOT_TOKEN, GUILD_ID, API_URL)
load_dotenv()

# Enable intents 
# DO NOT MESS WITH THIS OR THE BOT WILL NOT WORK. THE ENTIRE FILE WILL NOW WORK OF FIX
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
Token = os.getenv("DISCORD_TOKEN")

#Create a command in the cog or bot tree to work with bot commands in discord
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    try:
        #syncs the bot commands with the guild
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

#Async function to search and load all cog files
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded extension: {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')
async def main():
    async with bot:
        await load_extensions()
        await bot.start(Token)

#Run the bot with initialization loop
asyncio.run(main())
