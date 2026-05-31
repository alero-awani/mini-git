"""
search_lines_linear.py

Searches commits by number of lines edited using linear search.
Time Complexity: O(n) — scans every element once
Space Complexity: O(k) — where k is the number of matching commits
Reason: linear search requires no sorting beforehand, making it faster for a single
        search operation than sort + binary search which costs O(n log n) upfront.
Usage: python3 search_lines_linear.py
"""
from store import load

commits = load()

print("Search by lines edited:")
print("1. Greater than")
print("2. Less than")
print("3. Between")

choice = input("\nEnter choice: ")

results = []

if choice == "1":
    value = int(input("Greater than: "))
    for commit in commits:
        if commit["lines_edited"] > value:
            results.append(commit)

elif choice == "2":
    value = int(input("Less than: "))
    for commit in commits:
        if commit["lines_edited"] < value:
            results.append(commit)

elif choice == "3":
    lower = int(input("From: "))
    upper = int(input("To: "))
    for commit in commits:
        if lower <= commit["lines_edited"] <= upper:
            results.append(commit)

if results:
    print("\nResults:")
    for i, commit in enumerate(results):
        print(i, commit)
else:
    print("\nNo commits found in that range")
