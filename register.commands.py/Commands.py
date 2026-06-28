import os
import discord
from dotenv import load_dotenv

load_dotenv()

class SyncBot(discord.Client):
    async def setup_hook(self):
        # Load all command files from /src/commands
        for filename in os.listdir("./src/commands"):
            if filename.endswith(".py"):
                await self.tree.load_extension(f"src.commands.{filename[:-3]}")

        # Sync commands to your Discord server
        await self.tree.sync(guild=discord.Object(id=os.getenv("GUILD_ID")))
        print("Slash commands synced successfully.")

intents = discord.Intents.default()
client = SyncBot(intents=intents)

client.run(os.getenv("BOT_TOKEN"))
