"""
filter_author.py

Filters commits by author name using a linear search.
Time Complexity: Linear Search — O(n)
Space Complexity: O(1) - Best case, if no commits match, O(n) - Worst case, if all commits match
Reason: must check every element because there may be multiple matches.
Usage: python3 filter_author.py
Git command: git log --author="Alice"
"""
from store import load

commits = load()

author = input("Enter author name to filter by: ")

results = []  # will hold all matching commits

# linear search — must check every element because there may be multiple matches
for i, commit in enumerate(commits):
    if commit["author"] == author:   # check if this commit's author matches
        results.append((i, commit))  # store the index and the commit together

if results:
    print(f"\nCommits by {author}:")
    for i, commit in results:
        print(i, commit)
else:
    print(f"\nNo commits found for author: {author}")
