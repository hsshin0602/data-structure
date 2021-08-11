import heapq

nums=[4,1,7,3,8,5]
heap=[]

for i in nums:
    heapq.heappush(heap, i)
print(heap)

while heap:
    print(heapq.heappop(heap))
