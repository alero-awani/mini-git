"""
sort_author.py

Displays all commits sorted by author using merge sort.
Time Complexity: O(n log n) — guaranteed regardless of input order
Space Complexity: O(n) — merge sort creates new lists during each split and merge
Reason: string comparisons are costly per operation, merge sort minimises the total
        number of comparisons to O(n log n).
Usage: python3 sort_author.py
Git equivalent: git log --author (sorted alphabetically)
"""
from store import load
from helpers import merge_sort

commits = load()

commits = merge_sort(commits, "author")

print("Sort order:")
print("1. Ascending  (A → Z)")
print("2. Descending (Z → A)")

choice = input("\nEnter choice: ")

if choice == "2":
    commits = commits[::-1]   # reverse the sorted list for descending order

print(f"\nCommits sorted by author ({'descending' if choice == '2' else 'ascending'}):")
for i, commit in enumerate(commits):
    print(i, commit)
