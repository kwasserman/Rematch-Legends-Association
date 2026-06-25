
import os
import discord 
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
# Do not mess with this file, it is used to load the bot token and other sensitive information
# Only edit the .env file if you know what you are doing

load_dotenv()

Token = os.getenv("DISCORD_TOKEN")

#define intents(Permissions the bot request from Discord)
intents = discord.Intents.default()
intents.message_content = True #required for reading message content

#Initialize the bot with command prefix and intents(e.g /Help)
bot = commands.Bot(command_prefix='/', intents=intents)

#Event: Triggers when the bot is ready and successfully connected to Discord
git@bot.event

async def on_ready():
    print('Rematch League System is Online!!')
 
@bot.command(name='playping')

#Command: Triggers when someone types /command in Discord
#Command: /playping tiggers when someone types /playping in Discord
async def playping(ctx):
     await ctx.send('Pong!');

#Run the bot using token Do not mess with fumction or the bot will not work
bot.run(Token)