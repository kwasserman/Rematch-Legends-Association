import discord
from discord import app_commands
from discord.ext import commands

from src.services.api import check_registration


class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="regcheck",
        description="Check if a player is registered in the system."
    )
    async def regcheck(self, interaction: discord.Interaction, username: str):
        # Call your API
        data = await check_registration(username)

        # If API_URL is missing or API failed
        if data.get("error"):
            return await interaction.response.send_message(
                f"❌ API Error: {data['error']}",
                ephemeral=True
            )

        # If user is NOT registered
        if not data.get("registered"):
            return await interaction.response.send_message(
                f"❌ **{username}** is NOT registered.",
                ephemeral=False
            )

        # If user IS registered
        await interaction.response.send_message(
            f"✅ **{username}** is registered.\n"
            f"**Team:** {data.get('team', 'Unknown')}\n"
            f"**ID:** {data.get('id', 'N/A')}"
        )


async def setup(bot):
    await bot.add_cog(Register(bot))
