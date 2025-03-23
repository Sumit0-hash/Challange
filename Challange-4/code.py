from collections import Counter

def count_inversions(arr):
    """ Uses merge sort to count swaps needed. """
    if len(arr) < 2:
        return 0

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    inv_count = count_inversions(left) + count_inversions(right)

    i = j = 0
    temp = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            inv_count += len(left) - i
            j += 1

    arr[:] = temp + left[i:] + right[j:] 
    return inv_count

def min_swaps_to_transform(A, B):
    if Counter(A) != Counter(B):
        return -1

    pos_map = {char: [] for char in B}
    for i, char in enumerate(A):
        pos_map[char].append(i)

    mapped_positions = [pos_map[char].pop(0) for char in B]

    return count_inversions(mapped_positions)

# Input
N = int(input())
A, B = input().strip(), input().strip()

print(min_swaps_to_transform(A, B))
