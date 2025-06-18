from flask import Flask, request, jsonify
import base64
from PIL import Image
import io
import mood_detector  # sudah tidak pakai cv2

app = Flask(__name__)

@app.route('/api/detect-mood', methods=['POST'])
def detect_mood():
    try:
        image_data = request.json['image']
        print("Received image data")

        image_bytes = base64.b64decode(image_data.split(",")[1])
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")  # langsung jadi PIL

        mood_result = mood_detector.detect_mood(image)
        return jsonify({'mood': mood_result})
    except Exception as e:
        print(f"Error in detect_mood: {e}")
        return jsonify({'mood': 'Mood detection failed.'}), 500
