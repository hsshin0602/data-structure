import heapq
import sys

heap=[]
case=int(sys.stdin.readline())
for _ in range(case):
    num=int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num),num))
        print(heap)
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
        
