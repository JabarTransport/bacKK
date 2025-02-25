from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Load API key dari .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

app = Flask(__name__)
CORS(app)  # Izinkan akses dari frontend

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get("messages", [])

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
        json={"model": "llama3-70b-8192", "messages": messages}
    )

    return jsonify(response.json())

def handler(event, context):
    return app(event, context)


if __name__ == '__main__':
    app.run(debug=True)
