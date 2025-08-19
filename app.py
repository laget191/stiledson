import os
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Загружаем API ключ
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # можно заменить на gpt-4.1
        messages=[
            {"role": "system", "content": "Ты умный помощник, отвечай дружелюбно."},
            {"role": "user", "content": user_message},
        ]
    )

    bot_reply = response.choices[0].message.content
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

