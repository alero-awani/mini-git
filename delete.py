from store import load, save

commits = load()

print("Current commits:")
for i, commit in enumerate(commits):
    print(i, commit)

index = int(input("\nEnter index to delete: "))

removed = commits.pop(index)
save(commits)

print("\nDeleted:", removed)
print("\nUpdated list:")
for i, commit in enumerate(commits):
    print(i, commit)
