from collections import deque

def find_min_max_in_subarrays(array, window_size):
    """
    Find the minimum of the maximum values in each subarray of a given window size.

    Args:
        array : The input array of integers.
        window_size : The size of the sliding window.

    Returns:
        int: The minimum of the maximum values in each subarray.
    """

    if not array:
        raise ValueError("Array cannot be empty")
    if window_size > len(array):
        raise ValueError("Window size cannot be greater than array length")
    if window_size <= 0:
        raise ValueError("Window size must be a positive integer")

    max_deque = deque()

    window_maxima = []

    for i in range(window_size):
        while max_deque and array[max_deque[-1]] <= array[i]:
            max_deque.pop()
        max_deque.append(i)

    for i in range(window_size, len(array)):
        window_maxima.append(array[max_deque[0]])

        while max_deque and max_deque[0] <= i - window_size:
            max_deque.popleft()

        while max_deque and array[max_deque[-1]] <= array[i]:
            max_deque.pop()

        max_deque.append(i)
    window_maxima.append(array[max_deque[0]])

    return min(window_maxima)

try:
    window_size, array_length = map(int, input("Enter the window size and array length: ").split())
    if array_length <= 0:
        raise ValueError("Array length must be a positive integer")
    
    array = [int(input(f"Enter element {i+1}: ")) for i in range(array_length)]

    print("Minimum of maximum values:", find_min_max_in_subarrays(array, window_size))
except ValueError as e:
    print("Error:", e)
