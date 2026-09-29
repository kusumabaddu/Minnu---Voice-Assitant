conversation_history = []


def add_memory(user_message, assistant_message):

    conversation_history.append(
        f"User: {user_message}"
    )

    conversation_history.append(
        f"Minnu: {assistant_message}"
    )

    # Keep only the last 10 messages
    if len(conversation_history) > 10:

        del conversation_history[:-10]


def get_memory():

    return "\n".join(conversation_history)


def clear_memory():

    conversation_history.clear()