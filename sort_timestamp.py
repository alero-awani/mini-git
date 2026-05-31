"""
sort_timestamp.py

Displays all commits sorted by timestamp using insertion sort.
Time Complexity: O(n) best case (nearly sorted), O(n²) worst case (random order)
Space Complexity: O(1) — sorts in place, no extra lists created
Reason: a commit log is naturally nearly sorted by timestamp since new commits are
        always appended to the end with the current time. Insertion sort approaches
        O(n) on nearly sorted data, making it the most efficient choice here.
Usage: python3 sort_timestamp.py
Git equivalent: git log (default git log is sorted by timestamp descending)
"""
from store import load

commits = load()

# insertion sort by timestamp
for i in range(1, len(commits)):
    current = commits[i]
    j = i - 1
    while j >= 0 and commits[j]["timestamp"] > current["timestamp"]:
        commits[j + 1] = commits[j]
        j -= 1
    commits[j + 1] = current

print("Commits sorted by timestamp (ascending):")
for i, commit in enumerate(commits):
    print(i, commit)
