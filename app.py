from flask import Flask, jsonify

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def home():
    logger.info("Request to /")
    return jsonify({
        "app": "devops-flask-ci-demo",
        "status": "running",
        "message": "Hello, DevOps!"
    })


@app.route("/health")
def health():
    logger.info("Request to /health")
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)