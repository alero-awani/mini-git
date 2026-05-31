"""
list.py

Displays all current commits in the dataset.
Usage: python3 list.py
Git equivalent: git log
"""
from store import load

commits = load()

print("Current commits:")
for i, commit in enumerate(commits):
    print(i, commit)
