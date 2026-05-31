from store import load, save
from datetime import datetime

repo = input("Repo name: ")
author = input("Author: ")
#user does not input the timestamp, it is generated automatically when the commit is added. This is how it works in real git as well
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
description = input("Description: ")
lines_edited = int(input("Lines edited: "))

new_commit = {
    "repo": repo,
    "author": author,
    "timestamp": timestamp,
    "description": description,
    "lines_edited": lines_edited
}

commits = load()
commits.append(new_commit)
save(commits)

print("\nCommit added. Updated list:")
for i, commit in enumerate(commits):
    print(i, commit)
