from collections import deque
import sys

case=int(sys.stdin.readline())
graph=[[] for _ in range(case+1)]
for _ in range(case):
    arr=list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(arr)-1,2):
        graph[arr[0]].append((arr[j],arr[j+1]))
       
print(graph)
def BFS(start):
    visit=[-1]*(case+1)
    q=deque()
    q.append(start)
    visit[start]=0
    _max=[0,0]
    while q:
        a=q.popleft()
        for i, e in graph[a]:
            if visit[i]==-1:
                visit[i]=visit[a]+e
                q.append(i)
                print(visit[i])
                if _max[0] < visit[i]:
                    _max = visit[i], i
    return _max

dis,node=BFS(1)
dis,node=BFS(node)
print(dis)

