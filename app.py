import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API Flask funcionando!"})

@app.route('/sum/<int:a>/<int:b>')
def sum_numbers(a, b):
    return jsonify({"sum": a + b})

@app.route('/status')
def status():
    return jsonify({"status": "OK", "code": 200})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)