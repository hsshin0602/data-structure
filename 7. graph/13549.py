from collections import deque
import sys

N,K=map(int, sys.stdin.readline().split())
MAX=100001
arr=[-1] * MAX
q=deque()
q.append(N)
arr[N]=0
while q:
    x= q.popleft()
    if x==K:
        print(arr[K])
        break
    for i in (2*x,x-1,x+1): # 순서의 의미?
        if 0 <= i < MAX and arr[i]==-1:
                if i==2*x:
                    arr[i]=arr[x]
                    q.append(i) # i의 순서가 랜덤이라고 할때appendleft로 해야하는 이유
                else:
                    arr[i]=arr[x]+1
                    q.append(i)

