from langdetect import detect

session_memory = {
    "last_intent": None,
    "last_action": None
}

user_memory = {
    "preferred_language": "en",
    "past_appointments": []
}

def detect_language(text):
    try:
        lang = detect(text)
        if lang not in ["en", "hi", "ta"]:
            return "en"
        return lang
    except:
        return "en"