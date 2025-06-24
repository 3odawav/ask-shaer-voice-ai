from flask import Flask, request, send_file, jsonify
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route("/api/ask-shaer", methods=["POST"])
def ask_shaer():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        # هنا المفروض تربط بالذكاء الصناعي لو عايز (مثلاً GPT)
        response_text = f"الإجابة على سؤالك: {prompt}"

        # تحويل النص إلى صوت (مؤقت لحين ربط RVC)
        filename = f"output_{uuid.uuid4().hex}.mp3"
        tts = gTTS(response_text, lang='ar')
        tts.save(filename)

        return send_file(filename, mimetype="audio/mpeg")

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
