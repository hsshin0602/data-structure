import sys
from collections import deque

N,K=map(int, sys.stdin.readline().split())
arr=[0 for _ in range(100001)]

if N==K:
    print('0')
    exit()

def BFS(start):
    q=deque()
    q.append(start)
    while q:
        a=q.popleft()
        if 2*a < 100001 and arr[2*a]==0 and N != 2*a:
            arr[2*a]=arr[a]+1
            q.append(2*a)
        if a+1 < 100001 and arr[a+1]==0 and N != a+1:
            arr[a+1]=arr[a]+1
            q.append(a+1)
        if a-1 >= 0 and arr[a-1]==0 and N != a-1:
            arr[a-1]=arr[a]+1
            q.append(a-1)
        if arr[K]!=0:
            break
    return

BFS(N)
print(arr[K])

