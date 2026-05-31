"""
search_lines.py

Searches commits by number of lines edited using binary search.
Time Complexity: O(log n) for the binarysearch, O(n log n) for the merge sort
Space Complexity: O(n) for merge sort (creates new lists during sorting), O(1) for binary search (only uses 4 variables regardless of input size)
Reason: numeric field can be sorted, allowing binary search to find the boundary fast.
Usage: python3 search_lines.py
Git equivalent: git log --diff-filter
"""
from store import load
from helpers import merge_sort

commits = load()

# binary search requires the array to be sorted first
commits = merge_sort(commits, "lines_edited")

print("Search by lines edited:")
print("1. Greater than")
print("2. Less than")
print("3. Between")

choice = input("\nEnter choice: ")


def find_cutoff_above(commits, value):
    # binary search — finds the first index where lines_edited exceeds the value
    left = 0
    right = len(commits) - 1
    cutoff = len(commits)

    while left <= right:
        mid = (left + right) // 2
        if commits[mid]["lines_edited"] > value:
            cutoff = mid        # could be the boundary, check left for an earlier one
            right = mid - 1
        else:
            left = mid + 1      # not past value yet, move right

    return cutoff


def find_cutoff_below(commits, value):
    # binary search — finds the first index where lines_edited equals or exceeds the value
    left = 0
    right = len(commits) - 1
    cutoff = len(commits)

    while left <= right:
        mid = (left + right) // 2
        if commits[mid]["lines_edited"] >= value:
            cutoff = mid        # could be the boundary, check left for an earlier one
            right = mid - 1
        else:
            left = mid + 1      # not at value yet, move right

    return cutoff


results = []

if choice == "1":
    value = int(input("Greater than: "))
    cutoff = find_cutoff_above(commits, value)
    results = commits[cutoff:]

elif choice == "2":
    value = int(input("Less than: "))
    cutoff = find_cutoff_below(commits, value)
    results = commits[:cutoff]

elif choice == "3":
    lower = int(input("From: "))
    upper = int(input("To: "))
    lower_cutoff = find_cutoff_below(commits, lower)
    upper_cutoff = find_cutoff_above(commits, upper)
    results = commits[lower_cutoff:upper_cutoff]

if results:
    print("\nResults:")
    for i, commit in enumerate(results):
        print(i, commit)
else:
    print("\nNo commits found in that range")
