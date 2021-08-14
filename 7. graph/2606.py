import sys
from collections import deque

num=int(sys.stdin.readline())
edge=int(sys.stdin.readline())
graph=[[] for _ in range(num+1)]
visit=[0 for _ in range(num+1)]

for i in range(edge):
    a,b=map(int, sys.stdin.readline().split())
    if not a in  graph[b]:
        graph[b].append(a)
    if not b in graph[a]:
        graph[a].append(b)

def BFS(start):
    q=deque()
    q.append(start)
    visit[start]=1
    while q:
        k=q.popleft()
        for i in graph[k]:
            if visit[i] == 0:
                visit[i]=1
                q.append(i)
    return visit
arr=BFS(1)
cnt=-1
for i in range(1,len(arr)):
    if arr[i] == 1:
        cnt+=1
print(cnt)