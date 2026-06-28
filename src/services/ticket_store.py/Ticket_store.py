tickets = {}

def set_ticket(user_id: int, channel_id: int):
    """Store the user's ticket channel."""
    tickets[user_id] = channel_id

def get_ticket(user_id: int):
    """Return the user's ticket channel ID, or None."""
    return tickets.get(user_id)

def clear_ticket(user_id: int):
    """Remove the user's ticket from storage."""
    tickets.pop(user_id, None)