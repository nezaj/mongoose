import random

from .dummy import words
from .models import User

def generate_random_phrase():
    num_words = random.randint(3, 5)
    return ''.join([random.choice(words) for _ in range(num_words)])

def prepopulate_data(session):
    users = [
        User(id="1", email="admin@example.com", username="admin", password="admin", bio=generate_random_phrase()),
        User(id="2", email="joe@example.com", username="joe", password="joe", bio=generate_random_phrase()),
        User(id="3", email="moop@example.com", username="moop", password="moop", bio=generate_random_phrase())
    ]

    session.add_all(users)
    session.commit()
