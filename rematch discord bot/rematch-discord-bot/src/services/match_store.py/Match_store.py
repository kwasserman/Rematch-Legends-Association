match = {
    "active": False,
    "home": {"name": "Home", "score": 0},
    "away": {"name": "Away", "score": 0},
    "minute": 0,
    "events": []
}

def start_match(home, away):
    """
    Initializes a new match with home and away team names.
    Resets score, minute, and event list.
    """
    match["active"] = True
    match["home"] = {"name": home, "score": 0}
    match["away"] = {"name": away, "score": 0}
    match["minute"] = 0
    match["events"] = []

def set_minute(minute):
    """
    Updates the current match minute.
    """
    match["minute"] = minute

def add_event(team, player, event_type):
    """
    Adds an event to the match timeline.
    Example event:
    {
        "minute": 15,
        "team": "home",
        "player": "Joshua",
        "type": "goal"
    }
    """
    match["events"].append({
        "minute": match["minute"],
        "team": team,
        "player": player,
        "type": event_type
    })

    # Auto‑update score if event is a goal
    if event_type == "goal":
        match[team]["score"] += 1

def get_match():
    """
    Returns the full match dictionary.
    """
    return match
