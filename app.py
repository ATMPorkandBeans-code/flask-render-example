from flask import Flask, jsonify, render_template

app = Flask(__name__)

MESSAGES = [
    {"id": 1, "text": "Flask is running on Render!", "author": "Server"},
    {"id": 2, "text": "This is a simple full-stack example.", "author": "Server"},
    {"id": 3, "text": "Edit app.py to add your own data.", "author": "Server"},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/messages")
def get_messages():
    return jsonify(MESSAGES)


if __name__ == "__main__":
    app.run(debug=True)
