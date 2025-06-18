from deepface import DeepFace
from PIL import Image
import numpy as np

def detect_mood(pil_image):
    # Konversi gambar ke format yang bisa diproses oleh DeepFace
    image_array = np.array(pil_image.convert("RGB"))

    mood_translation = {
        "happy": "Bahagia",
        "sad": "Sedih",
        "angry": "Marah",
        "fear": "Takut",
        "neutral": "Normal"
    }

    try:
        result = DeepFace.analyze(image_array, actions=['emotion'], enforce_detection=False)

        if isinstance(result, list):
            result = result[0]

        emotions = result["emotion"]

        emotions.pop("disgust", None)
        emotions.pop("surprise", None)

        if emotions:
            dominant_mood = max(emotions, key=emotions.get)
            return mood_translation.get(dominant_mood, "Mood tidak teridentifikasi.")
        else:
            return "Mood tidak teridentifikasi."
    except Exception as e:
        print(f"Error dalam analisis ekspresi: {e}")
        return "Analisis ekspresi gagal."
