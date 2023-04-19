#!/usr/bin/python3

from models.state import State
from models.city import City
from models import storage
import os

try:
    os.remove("file.json")
except Exception:
    pass
storage.new_object()
if __name__ == '__main__':

    lagos = State(name="Lagos State")
    lagos.save()
    edo = State(name="Edo State")
    edo.save()
    benin = City(name="Benin", state_id=edo.id)
    benin.save()
    auchi = City(name="Auchi", state_id=edo.id)
    auchi.save()
    ekpoma = City(name="Ekpoma", state_id=edo.id)
    ekpoma.save()
    vi = City(name="VI", state_id=lagos.id)
    vi.save()
    
    print(edo.cities)
    print(lagos.cities)
