import json
import os
from commit import commits

def load():
    if os.path.exists("commits.json"):
        with open("commits.json", "r") as f:
            return json.load(f)
    else: 
        return commits

def save(data):
    with open("commits.json", "w") as f:
        json.dump(data, f, indent=4)
