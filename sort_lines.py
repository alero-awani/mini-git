from store import load, save
from helpers import merge_sort

commits = load()

commits = merge_sort(commits, "lines_edited")  # pass "lines_edited" as the field to sort by

save(commits)

print("Commits sorted by lines edited (ascending):")
for i, commit in enumerate(commits):
    print(i, commit)
