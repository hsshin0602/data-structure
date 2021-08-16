from collections import deque
import sys

N,M=map(int, sys.stdin.readline().split())
dx=[0,1,0,-1]
dy=[1,0,-1,0]

graph=[]
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
visit=[]
for _ in range(N):
    visit.append(list(0 for _ in range(M)))

def BFS(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]='#'
    visit[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visit[nx][ny]==0:
                    graph[nx][ny]='#'
                    visit[nx][ny]=visit[x][y]+1 #가중치문제랑 비슷!!!
                    q.append((nx,ny))
    return 
                    
BFS(0,0)
print(visit[N-1][M-1])