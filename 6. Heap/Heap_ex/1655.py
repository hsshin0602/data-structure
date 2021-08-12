import heapq
import sys

left_max=[]
right_min=[]
case= int(sys.stdin.readline())
for i in range(case):
    num=int(sys.stdin.readline())
    if len(left_max) == len(right_min):
        heapq.heappush(left_max, (-num,num))
    else:
        heapq.heappush(right_min, (num,num))
    
    if right_min and left_max[0][1] > right_min[0][1]:
        left_value=heapq.heappop(left_max)[1]
        right_value=heapq.heappop(right_min)[1]
        heapq.heappush(left_max, (-right_value,right_value))
        heapq.heappush(right_min, (left_value,left_value))
    print(left_max[0][1])
