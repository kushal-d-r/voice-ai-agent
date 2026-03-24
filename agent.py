from db.appointments import book_appointment, cancel_appointment, reschedule_appointment
from memory import session_memory, user_memory

def agent(text):
    text = text.lower()

    tools = {
        "book": lambda: book_appointment(user_memory),
        "cancel": cancel_appointment,
        "reschedule": reschedule_appointment
    }

    if any(word in text for word in ["book", "appointment"]):
        tool = "book"
    elif "cancel" in text:
        tool = "cancel"
    elif "reschedule" in text:
        tool = "reschedule"
    else:
        return "Sorry, I didn't understand your request"

    print(f"[Agent Decision] Calling tool: {tool}")

    response = tools[tool]()

    session_memory["last_intent"] = tool
    session_memory["last_action"] = response

    return response