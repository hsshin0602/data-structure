import sys
from collections import deque

case=int(sys.stdin.readline())
graph=[[] for _ in range(case+1)]
for i in range(case-1):
    arr=list(map(int,sys.stdin.readline().split()))
    graph[arr[0]].append((arr[1],arr[2]))
    graph[arr[1]].append((arr[0],arr[2]))
print(graph)
def BFS(start):
    visit=[-1]*(case+1)
    q=deque()
    q.append(start)
    visit[start]=0
    tmpmax=[0,0]
    while q:
        a=q.popleft()
        for i, e in graph[a]:
            if visit[i] == -1:
                visit[i]=visit[a]+e
                q.append(i)
            if tmpmax[0] < visit[i]:
                tmpmax = visit[i],i
    return tmpmax

dis,node = BFS(1)
dis,node = BFS(node)
print(dis)
