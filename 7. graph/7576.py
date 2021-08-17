from collections import deque
import sys

M,N=map(int, sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(x,y):
    arr=[]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                arr.append((nx,ny))
    return arr

q=deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            q.append((i,j))
cnt=-1
while q:
    for _ in range(len(q)):
        x,y=q.popleft()
        for arr in BFS(x,y): # 주변이 0인 곳의 위치
            q.append(arr)
    cnt+=1

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            print('-1')
            exit()
print(cnt)


            
        