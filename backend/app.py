from flask import Flask, jsonify, request
import requests
import time

app = Flask(__name__)


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/check")
def check_website():

    url = request.args.get("url")

    if not url:
        return jsonify({
            "healthy": False,
            "error": "URL is required"
        }), 400

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:

        start = time.time()

        response = requests.get(
            url,
            timeout=5
        )

        end = time.time()

        return jsonify({
            "healthy": response.ok,
            "url": url,
            "status": response.status_code,
            "response_time": round((end - start) * 1000, 2)
        })

    except requests.RequestException as e:

        return jsonify({
            "healthy": False,
            "url": url,
            "error": "Website is unreachable"
        })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
