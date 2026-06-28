import discord
from discord import app_commands
from discord.ext import commands

from src.services.ticket_store import (
    set_ticket,
    get_ticket,
    clear_ticket
)


class Ticket(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ticket_open",
        description="Open a private support ticket."
    )
    async def ticket_open(self, interaction: discord.Interaction):
        user = interaction.user
        user_id = user.id

        # Check if user already has a ticket
        existing = get_ticket(user_id)
        if existing:
            return await interaction.response.send_message(
                " You already have an open ticket.",
                ephemeral=True
            )

        # Create private channel
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True)
        }

        channel = await interaction.guild.create_text_channel(
            name=f"ticket-{user.name}",
            overwrites=overwrites
        )

        # Store ticket
        set_ticket(user_id, channel.id)

        await interaction.response.send_message(
            f" Ticket created: {channel.mention}",
            ephemeral=True
        )

    @app_commands.command(
        name="ticket_close",
        description="Close your open ticket."
    )
    async def ticket_close(self, interaction: discord.Interaction):
        user_id = interaction.user.id

        # Check if user has a ticket
        channel_id = get_ticket(user_id)
        if not channel_id:
            return await interaction.response.send_message(
                " You do not have an open ticket.",
                ephemeral=True
            )

        # Delete the channel
        channel = interaction.guild.get_channel(channel_id)
        if channel:
            await channel.delete()

        # Clear storage
        clear_ticket(user_id)

        await interaction.response.send_message(
            " Your ticket has been closed.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Ticket(bot))