def count_treasures(treasure_map, search_ranges):
    length = len(treasure_map)
    nums = [0] * (length + 1) 

    for pos in range(1, length + 1):
        nums[pos] = nums[pos - 1] + (1 if treasure_map[pos - 1] == 'T' else 0)
    treasure_counts = []
    for start, end in search_ranges:
        treasure_count = nums[end] - nums[start - 1]
        treasure_counts.append(treasure_count)
    return treasure_counts

treasure_map = input("enter the treasure map: ").strip()
num_queries = int(input("Number of ranges:"))

search_ranges = []
print("Enter the ranges:")
for _ in range(num_queries):
    start, end = map(int, input().split())
    search_ranges.append((start, end))

print("Results:")
for count in count_treasures(treasure_map, search_ranges):
    print(count)