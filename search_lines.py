from store import load
from helpers import merge_sort

commits = load()

# binary search requires the array to be sorted first
commits = merge_sort(commits, "lines_edited")

threshold = int(input("Show commits where lines edited is greater than: "))

# binary search — find the first index where lines_edited exceeds the threshold
left = 0
right = len(commits) - 1
cutoff = len(commits)  # default to end of list if nothing exceeds threshold

while left <= right:
    mid = (left + right) // 2              # find the middle index

    if commits[mid]["lines_edited"] > threshold:
        cutoff = mid                        # this could be our boundary, but check left half for an earlier one
        right = mid - 1
    else:
        left = mid + 1                      # not past threshold yet, move right

results = commits[cutoff:]                  # everything from the cutoff onwards exceeds the threshold

if results:
    print(f"\nCommits with more than {threshold} lines edited:")
    for i, commit in enumerate(results):
        print(i, commit)
else:
    print(f"\nNo commits found with more than {threshold} lines edited")
