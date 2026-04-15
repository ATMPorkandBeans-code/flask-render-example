import os

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use DATABASE_URL env var in production (Render), SQLite locally
database_url = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
# SQLAlchemy requires postgresql:// instead of postgres://
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "text": self.text, "author": self.author}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/messages")
def get_messages():
    messages = Message.query.order_by(Message.id).all()
    return jsonify([m.to_dict() for m in messages])


if __name__ == "__main__":
    app.run(debug=True)
