from collections import deque
import sys

M,N= map(int, sys.stdin.readline().split())

graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

q=deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            q.append((i,j))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def BFS():
    arr=[]
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    q.append((nx,ny))
    return graph

BFS()
result=0
for i in graph:
    for j in i:
        if j==0:
            print('-1')
            exit()
        else:
            result=max(j,result)
print(result-1)

