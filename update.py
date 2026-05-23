from store import load, save
from datetime import datetime

commits = load()

print("Current commits:")
for i, commit in enumerate(commits):
    print(i, commit)

index = int(input("\nEnter index to update: "))

print("\nWhat field do you want to update?")
print("1. repo")
print("2. author")
print("3. description")
print("4. lines_edited")

field_map = {
    "1": "repo",
    "2": "author",
    "3": "description",
    "4": "lines_edited"
}

choice = input("\nEnter number: ")
field = field_map[choice]

new_value = input(f"Enter new value for {field}: ")

if field == "lines_edited":
    new_value = int(new_value)

# updates the value of an attribute
commits[index][field] = new_value

# Updating the timestamp of the commit to show the time the commit was updated
commits[index]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")

# the recent commit should always be at the end of the list. so it is removed from its
# current position and added to the end of the list. This is how it is done in real
# git
updated_commit = commits.pop(index)
commits.append(updated_commit)
save(commits)

print("\nUpdated commit:")
for i, commit in enumerate(commits):
    print(i, commit)

