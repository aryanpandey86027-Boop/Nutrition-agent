import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL   = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
GROQ_URL     = os.getenv("GROQ_URL", "https://api.groq.com/openai/v1/chat/completions")


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """Proxy chat requests to Groq so the API key stays server-side."""
    body = request.get_json(force=True)
    messages = body.get("messages", [])
    if not messages:
        return jsonify({"error": "messages are required"}), 400

    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": body.get("temperature", 0.7),
        "max_tokens": body.get("max_tokens", 1500),
    }

    try:
        resp = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return jsonify({"content": content})
    except requests.exceptions.HTTPError as e:
        try:
            err_body = e.response.json()
            msg = err_body.get("error", {}).get("message", str(e))
        except Exception:
            msg = str(e)
        return jsonify({"error": msg}), e.response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 503


if __name__ == "__main__":
    app.run(debug=True, port=5000)
