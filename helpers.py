# Space: O(log n)
def merge_sort(arr, key):
    # base case: a list of 0 or 1 elements is already sorted, nothing to do
    if len(arr) <= 1:
        return arr

    # find the middle index to split the list into two halves
    mid = len(arr) // 2

    # recursively sort the left half
    left = merge_sort(arr[:mid], key)

    # recursively sort the right half
    right = merge_sort(arr[mid:], key)

    # merge the two sorted halves back together
    return merge(left, right, key)

# Space: O(n)
def merge(left, right, key):
    result = []  # this will hold the merged, sorted elements
    i = 0        # pointer for the left half
    j = 0        # pointer for the right half

    # compare elements from both halves using whichever field was passed in
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])  # left value is smaller or equal, add it first
            i += 1                  # move left pointer forward
        else:
            result.append(right[j]) # right value is smaller, add it first
            j += 1                  # move right pointer forward

    # if any elements remain in the left half, add them all
    result += left[i:]

    # if any elements remain in the right half, add them all
    result += right[j:]

    return result

#Space Complexity: O(log n) + O(n) = O(n)