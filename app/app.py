from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

r = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379)

@app.route("/")
def home():
    visits = r.incr("visits")
    return jsonify({"visits": visits})

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
