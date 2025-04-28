import heapq

# It is the min heap implementation
heap = [4, 7, 3, -2, 1, 0]
print(heap)

heapq.heapify(heap)
print(heap)
print('-'*80)

nums = [4, 7, 3, -2, 1, 0]
heap = []
for value in nums:
    heapq.heappush(heap, value)
print(heap)

while heap:
    print(heapq.heappop(heap))
