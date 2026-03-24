import time
from speech.stt import speech_to_text
from speech.tts import text_to_speech
from memory import detect_language, session_memory, user_memory
from agent import agent
from scheduler import outbound_reminder

if __name__ == "__main__":
    print("🎤 Processing audio...")

    start = time.time()

    text = speech_to_text("audio.wav")
    mid1 = time.time()

    print("User:", text)

    lang = detect_language(text)
    print("Language:", lang)

    response = agent(text)
    mid2 = time.time()

    print("Agent:", response)
    print("Session Memory:", session_memory)
    print("User Memory:", user_memory)

    tts_lang = lang if lang in ["en", "hi", "ta"] else "en"
    text_to_speech(response, tts_lang)

    end = time.time()

    print(f"STT Latency: {mid1 - start:.2f}s")
    print(f"Agent Latency: {mid2 - mid1:.2f}s")
    print(f"TTS Latency: {end - mid2:.2f}s")
    print(f"Total Latency: {end - start:.2f}s")

    print("\n📞 Outbound Mode:")
    print(outbound_reminder())