# Array

An array stores elements in **contiguous (side-by-side) memory slots**, numbered by index.

```
index:  [0]        [1]        [2]        [3]        [4]
data:   commit_A   commit_B   commit_C   commit_D   commit_E
```

| Operation | Speed | Why |
|---|---|---|
| Add (to end) | O(1) | Just place it at the next open slot |
| Delete by index | O(n) | You must shift every element after it left by one |
| Update by index | O(1) | You jump directly to the slot — no searching |
| Sort | Natural fit | All classic sorting algorithms are designed for arrays |
| Binary Search | Requires it | Binary search needs to jump to the middle — only arrays allow that |

## Why Array?

Because our program needs **index-based access** for delete and update, and **random access** is a requirement for binary search. The array is the only structure in this group that satisfies all five operations. Linked lists lose because update becomes O(n) and binary search becomes impractical. Stacks and queues don't support index access at all.

---

# Sorting Algorithms

## Bubble Sort — O(n²)

Repeatedly compares adjacent pairs and swaps them if out of order. Keeps "bubbling" the largest value to the end.

```
[5, 3, 1, 4] → compare pairs → [3, 1, 4, 5] → repeat → [1, 3, 4, 5]
```

- Simple to write and explain
- Slow on large data
- Best used when: **small dataset, teaching purposes**

---

## Insertion Sort — O(n²) worst, O(n) best

Takes one element at a time and **inserts it into the correct position** in the already-sorted portion.

```
[5, 3, 1, 4]
→ take 3, insert before 5  → [3, 5, 1, 4]
→ take 1, insert at front  → [1, 3, 5, 4]
→ take 4, insert before 5  → [1, 3, 4, 5]
```

- Gets **very fast when data is nearly sorted** — approaches O(n)
- Best used when: **data that is already mostly in order**

---

## Merge Sort — O(n log n) always

Splits the array in half repeatedly, sorts each half, then **merges** them back together.

```
[5, 3, 1, 4]
→ split → [5, 3] and [1, 4]
→ split → [5][3] and [1][4]
→ merge → [3, 5] and [1, 4]
→ merge → [1, 3, 4, 5]
```

- Guaranteed fast regardless of input order
- Best used when: **data is unpredictable, accuracy matters, larger datasets**

---

## Matching Each Algorithm to an Attribute

| Attribute | Type | Algorithm | Why |
|---|---|---|---|
| **Timestamp** | Date/time | **Insertion Sort** | A commit log is naturally almost-sorted by time — new commits get added in order. Insertion sort is fastest on nearly-sorted data (approaches O(n)) |
| **Lines Edited** | Integer | **Merge Sort** | Numbers can vary wildly (1 line to 10,000 lines). No assumption about order. Merge sort guarantees O(n log n) regardless |
| **Author** | String | **Bubble Sort** | Small dataset (5 elements), alphabetical comparison, simple to demonstrate. The slowness of O(n²) doesn't matter here |

## One-Line Answer for Each

- **Insertion sort on timestamp** — because a commit log is almost always already in chronological order, and insertion sort is at its fastest on nearly-sorted data.
- **Merge sort on lines edited** — because numeric values have no predictable order, and merge sort's O(n log n) is guaranteed regardless of input.
- **Bubble sort on author** — because the dataset is small (5 elements), and the simplicity of bubble sort is appropriate when performance isn't a concern.

---

# Why a List of Dictionaries for the Dataset?

We need **two things at once**:

| Need | Solved by |
|---|---|
| Index-based access (delete, update, binary search) | The **list** — gives us `commits[2]` |
| Named fields (readable, no magic numbers) | The **dictionary** — gives us `commit["author"]` |

A list of dictionaries gives us both. It's the simplest structure that satisfies all our operations without classes or imports.

---

# Why Timestamp Cannot Be Updated — And Why That Matters for Sorting

## In Real Git — Commits Are Immutable

In real git, this situation cannot happen. Once a commit is made, it is never modified. It gets a permanent hash based on its content and timestamp.

When you run `git commit --amend`, git doesn't update the old commit — it **destroys it and creates a brand new one** with a new hash and a new timestamp. The old commit is gone.

So a real commit log is **always in chronological order** by design — the data structure enforces it.

## In Our Project

In `update.py`, timestamp is intentionally left out of the update options:

```python
field_map = {
    "1": "repo",
    "2": "author",
    "3": "description",
    "4": "lines_edited"     # timestamp is not here
}
```

If timestamps could be changed arbitrarily across multiple commits, the array could look like this:

```
[2024-01-20, 2024-01-08, 2024-01-25, 2024-01-01, 2024-01-15]
```

That is random order — insertion sort loses its advantage entirely and you are back to O(n²) with no benefit. In that case **merge sort would be the honest choice** because it guarantees O(n log n) regardless of how scrambled the data is.

## The Rule This Teaches

> The right sorting algorithm depends on the **nature of your data**, not just the data type.

| Timestamp data state | Best algorithm | Why |
|---|---|---|
| Always append-only (real git) | Insertion Sort | Nearly sorted guaranteed |
| Updates allowed, timestamps change | Merge Sort | No ordering assumption can be made |

Because we locked timestamp out of updates, our nearly-sorted assumption holds and insertion sort remains justified.

---

# Filtering By Description

`description` is a string — the same type as `author`. The assignment requires sorting by at least three attributes of **distinct types**. We already satisfy that with:

- `timestamp` → date/time
- `author` → string
- `lines_edited` → integer

Adding a sort by description would be a fourth sort on a type we already have. It would not add a new distinct type to our justification.

More importantly, sorting descriptions alphabetically carries **no useful meaning**:

```
"add dark mode"
"fix crash on startup"
"fix login bug"
"optimize query"
"refactor auth module"
```

Nobody reads a commit log in alphabetical order by description. It tells you nothing about history, size, or authorship.

## The One Exception — Conventional Commits

If every description used a category prefix:

```
"feat: add dark mode"
"fix: crash on startup"
"fix: login bug"
"refactor: auth module"
```

Sorting alphabetically would group all `feat:` together and all `fix:` together — which is useful. This is a real industry standard called **Conventional Commits**.

## What Description Is Actually For — Filtering

If someone wants to find commits by description, that is a **search or filter** problem, not a sort problem:

```
filter commits where description contains "fix"
```

This is more useful than sorting alphabetically. Sorting reorders the whole list. Filtering finds exactly what you are looking for.
