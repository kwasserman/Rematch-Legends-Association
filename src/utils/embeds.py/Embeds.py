import discord

def match_embed(match):
    """
    Builds a clean embed showing match status, score, minute, and events.
    """

    # Build event list text
    events_text = "\n".join(
        f"{e['minute']}' — {e['team'].capitalize()} — {e['player']} ({e['type']})"
        for e in match["events"]
    )

    if not events_text:
        events_text = "No events yet."

    # Create embed
    embed = discord.Embed(
        title=f"{match['home']['name']} vs {match['away']['name']}",
        description=f"**Score:** {match['home']['score']} - {match['away']['score']}",
        color=0x00AEFF
    )

    embed.add_field(name="Minute", value=f"{match['minute']}'", inline=True)
    embed.add_field(name="Events", value=events_text, inline=False)

    return embed
