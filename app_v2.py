from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/v2/hello")
def hello():
    return jsonify({"msg": "Hello from app v2"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("FLASK_PORT", 5001))
