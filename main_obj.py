#!/usr/bin/python3
"""."""

from models import storage
from models.state import State


if __name__ == '__main__':
    State(name="Edo State").save()
    State(name="Lagos State").save()

    data = storage.all(State)
    print(data)
