import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")
BASE_URL = "https://api.elevenlabs.io/v1"

HEADERS = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

def get_voices():
    response = requests.get(f"{BASE_URL}/voices", headers={"xi-api-key": API_KEY})
    if response.status_code == 200:
        return response.json()["voices"]
    else:
        raise Exception(f"Error fetching voices: {response.text}")

def text_to_speech(text, voice_id, output_path="output.mp3"):
    url = f"{BASE_URL}/text-to-speech/{voice_id}"
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        raise Exception(f"TTS failed: {response.text}")
