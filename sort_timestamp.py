from store import load, save

commits = load()

# insertion sort by timestamp
for i in range(1, len(commits)):
    current = commits[i]
    j = i - 1
    while j >= 0 and commits[j]["timestamp"] > current["timestamp"]:
        commits[j + 1] = commits[j]
        j -= 1
    commits[j + 1] = current

save(commits)

print("Commits sorted by timestamp (ascending):")
for i, commit in enumerate(commits):
    print(i, commit)
