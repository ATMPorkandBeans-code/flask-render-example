"""
Seed the database with initial data.

Usage:
    python seed.py
"""

from app import app, db, Message

SEED_MESSAGES = [
    {"text": "Flask is running on Render!", "author": "Server"},
    {"text": "This is a simple full-stack example.", "author": "Server"},
    {"text": "Edit app.py to add your own data.", "author": "Server"},
]


def seed():
    with app.app_context():
        db.create_all()

        if Message.query.count() > 0:
            print("Database already seeded — skipping.")
            return

        for data in SEED_MESSAGES:
            db.session.add(Message(**data))

        db.session.commit()
        print(f"Seeded {len(SEED_MESSAGES)} messages.")


if __name__ == "__main__":
    seed()
