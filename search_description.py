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
