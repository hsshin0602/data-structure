import sys
from collections import deque

case=int(sys.stdin.readline())
graph=[[] for _ in range(case+1)]
parent=[0 for _ in range(case+1)]

for i in range(case-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS():
    q=deque()
    q.append(1)
    while q:
        node=q.popleft()
        for i in graph[node]:
            if parent[i]==0:
                parent[i]=node
                q.append(i)
    return parent

BFS()
for i in parent[2:]:
    print(i)

def DFS(start,graph,parent):
    for i in graph[start]:
        if parent[i] == 0:
            parent[i]=start
            DFS(i, graph, parent)

DFS(1, graph, parent)
for i in parent[2:]:
    print(i)