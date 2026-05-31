"""
search_description.py

Searches commits by a keyword in the description using a linear search.
Time Complexity: Linear Search — O(n)
Space Complexity: O(1) - Best case, if no commits match, O(n) - Worst case, if all commits match
Reason: descriptions are free-form text and cannot be sorted, so binary search is not possible.
        must also check every element in case there are multiple matches.
Usage: python3 search_description.py
Git equivalent: git log --grep="keyword"
"""
from store import load

commits = load()

keyword = input("Enter keyword to search in description: ")

results = []  # will hold all matching commits

# linear search — descriptions are free-form text, cannot be sorted for binary search
for i, commit in enumerate(commits):
    if keyword.lower() in commit["description"].lower():  # case-insensitive match
        results.append((i, commit))                       # store index and commit

if results:
    print(f"\nCommits where description contains '{keyword}':")
    for i, commit in results:
        print(i, commit)
else:
    print(f"\nNo commits found with keyword: {keyword}")