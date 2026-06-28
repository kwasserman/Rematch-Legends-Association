import aiohttp
import os

API_URL = os.getenv("API_URL")

async def check_registration(username: str):
    """
    Calls your website API to check if a player is registered.
    Expected API response example:
    {
        "registered": true,
        "team": "Team Name",
        "id": 12345
    }
    """

    if not API_URL:
        return {"registered": False, "error": "API_URL is not set"}

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{API_URL}/registration",
            params={"username": username}
        ) as resp:

            # If the API fails or returns non‑JSON, avoid crashing the bot
            try:
                return await resp.json()
            except:
                return {"registered": False, "error": "Invalid API response"}
