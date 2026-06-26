import discord
from dotenv import load_dotenv
from discord.ext import commands
import os


load_dotenv()




class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/', intents=discord.Intents.default())

    async def setup_hook(self):
        # Target and open the seperate cog folder file structure
        #syntax for loading the cog file (await self.load_extension('cogs.<filename>')))
        #all cogs must be loaded in the main.py file to work properly
        #All functions must be in the Cogs folder to work properly, if they are not in the cogs folder they will not work
        #and in thier respective files they must be in a class that is a subclass of commands.Cog and have the setup function to load the cog
       await self.load_extension('cogs.announcement_cod')

       #sync the configuration maps layout directly up to the global discord server
       await self.tree.sync()
       print('Commands synced successfully! globally')

    async def on_ready(self):
        print(f'Rematch League System is Online!! Logged in as {self.user} (ID: {self.user.id})')
        
bot = MyBot()
token = os.getenv('DISCORD_TOKEN')
if token is None:
    # Make sure to install python-dotenv if you want to load environment variables from a .env file
    raise ValueError("DISCORD_TOKEN environment variable is not set")
bot.run(token)

