from collections import deque
import sys

N,K=map(int, sys.stdin.readline().split())
arr=[-1]*100001

def BFS():
    cnt=0
    result=100000
    q=deque()
    q.append(N)
    arr[N]=0
    while q:
        x=q.popleft()
        if x==K:
            cnt+=1
        for i in (x+1,x-1,2*x):
            if 0 <= i <= 100000:
                if arr[i]==-1 or arr[i]==arr[x]+1:
                    arr[i]=arr[x]+1
                    q.append(i)
    return cnt

cnt=BFS()
print(arr[K])
print(cnt)



