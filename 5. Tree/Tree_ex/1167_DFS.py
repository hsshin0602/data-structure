from collections import deque
import sys

case=int(sys.stdin.readline())
graph=[[] for _ in range(case+1)]
for _ in range(case):
    arr=list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(arr)-1,2):
        graph[arr[0]].append((arr[j],arr[j+1]))
       
def DFS(start):
    if visit[start]== -1:
        visit[start]=0
    for i,e in graph[start]:
        if visit[i] == -1:
            visit[i]=visit[start]+e
            DFS(i)
            
visit=[-1]*(case+1)
DFS(1)
tmpmax=0
idx=0
for i in range(len(visit)):
    if tmpmax < visit[i]:
        tmpmax=visit[i]
        idx=i
visit=[-1]*(case+1)
DFS(idx)
print(max(visit))


