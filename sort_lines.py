"""
sort_lines.py

Displays all commits sorted by lines edited using merge sort.
Time Complexity: O(n log n) — guaranteed regardless of input order
Space Complexity: O(n) — merge sort creates new lists during each split and merge
Reason: lines edited values are unpredictable with no ordering assumption, merge sort's
        guaranteed O(n log n) is the safest choice regardless of the data.
Usage: python3 sort_lines.py
Git equivalent: git log --stat (shows lines changed per commit)
"""
from store import load
from helpers import merge_sort

commits = load()

commits = merge_sort(commits, "lines_edited")  # pass "lines_edited" as the field to sort by

print("Commits sorted by lines edited (ascending):")
for i, commit in enumerate(commits):
    print(i, commit)
