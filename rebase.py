# Before rebase:
# main:    A - B - C
# feature:         B - D - E - F

commits_to_replay = ["D", "E", "F"]

# Step 1: push commits onto stack newest first, so oldest ends up on top
stack = []
for commit in reversed(commits_to_replay):
    stack.append(commit)

print("Stack (top is right):", stack)  # ['F', 'E', 'D'] — D is on top

# Step 2: reset to new base
rebased = ["A", "B", "C"]

# Step 3: pop and replay onto new base
while stack:
    commit = stack.pop()        # pops D first, then E, then F
    rebased.append(commit + "'")  # D', E', F' — replayed on new base

print("After rebase:", rebased)  # ['A', 'B', 'C', "D'", "E'", "F'"]
