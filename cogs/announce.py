import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime, timezone

class AnnounceModel(discord.ui.Modal, title="📢 Create Server Announcement"):

    
   #gset foarm fields
   announcement_title = discord.ui.TextInput(
       label="Announcement From the Admin Team",
       placeholder="Enter the title of the announcement",
       style=discord.TextStyle.long,
       required=True,
       max_length=120
   )

   #Content for the announcement
   announcement_content = discord.ui.TextInput(
       label="Announcement Body Content",
       placeholder="Enter the content of the announcement",
       style=discord.TextStyle.long,
       required=True,
       max_length=2000
   )

   def __init__(self, target_channel: discord.TextChannel):
       super().__init__()
       self.target_channel = target_channel 

    #do somwthing when an admin clicks submit
   async def on_submit(self, interaction: discord.Interaction):
        #builds the popout
        embed = discord.Embed(
            title=self.announcement_title.value,
            description=self.announcement_content.value,
            color=0x2f3136,  # Dark gray color
            timestamp=datetime.now(timezone.utc)  # Current UTC time
        )

        embed.set_author(name="Rematch League System", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)

        #Safely pulls the icon from discord if it exists, otherwise sets it to None to avoid errors

        guild_icon = interaction.guild.icon.url if interaction.guild.icon else None

        #footer for the embed
        embed.set_footer(text="RLS Broadcast System", icon_url=guild_icon)

        try:
            # send the embed to the target channel
            await self.target_channel.send(content="🚨 Important Information Incoming Please Stand By | @everyone",embed=embed)
            
            # send a confirmation message to the user who submitted the modal and it closes the modal
            await interaction.response.send_message(f"✅ Announcement sent successfully! Channel: {self.target_channel.mention}", 
                                                    ephemeral=True
             )
        except Exception as e:
            print (f"Error handling modal submission: {e}")
            await interaction.response.send_message(
                "❌ Failed to send announcement. Please check bot channel permissions", 
                                                    ephemeral=True
             )

# Move this class to the top level, outside of AnnounceModel and any methods
class AnnouncementCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="announce", description="Create a server announcement")
    @app_commands.describe(channel="The channel to send the announcement to")
    async def announce(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ You do not have permission to use this command.", ephemeral=True)
            return

        model_popup = AnnounceModel(target_channel=channel)
        await interaction.response.send_modal(model_popup)

# cogs/announcement_cod.py
async def setup(bot):
    await bot.add_cog(AnnouncementCog(bot))