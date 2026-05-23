from store import load, save
from helpers import merge_sort

commits = load()

commits = merge_sort(commits, "author")  # pass "author" as the field to sort by

save(commits)

print("Commits sorted by author (ascending):")
for i, commit in enumerate(commits):
    print(i, commit)
