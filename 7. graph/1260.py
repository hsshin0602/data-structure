from collections import deque
import sys
sys.setrecursionlimit(10**9)

N, M, start = map(int, sys.stdin.readline().split())
graph=[[]for _ in range(N+1)]

for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    if not b in graph[a]:
        graph[a].append(b)
    if not a in graph[b]:
        graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort(reverse=False)

parent=[]
def DFS(start):
    parent.append(start)
    for i in graph[start]:
        if i not in parent:
            DFS(i)
    return parent 
result_DFS=DFS(start)
print(*result_DFS)

def BFS(start):
    q=deque()
    q.append(start)
    visit=[]
    while q:
        k=q.popleft()
        if k not in visit:
            visit.append(k)
            for j in graph[k]:
                q.append(j)
    return visit
result_BFS=BFS(start)
print(*result_BFS)


