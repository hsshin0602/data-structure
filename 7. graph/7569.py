from collections import deque
import sys

M,N,H=map(int, sys.stdin.readline().split())
tomato=[]
graph=[]
for _ in range(H):
    a=len(graph)
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    tomato.append(graph[a:len(graph)]) #슬라이싱은 인덱스를 기준

print(tomato)
q=deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k]==1:
                q.append((i,j,k))

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
def BFS():
    while q:
        x,y,z=q.popleft()
        for i in range(6):
            nx=x+dx[i] #H
            ny=y+dy[i] #N
            nz=z+dz[i] #M
            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if tomato[nx][ny][nz]==0:
                    tomato[nx][ny][nz]=tomato[x][y][z]+1
                    q.append((nx,ny,nz))
    return
BFS()
result=0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k]==0:
                print('-1')
                exit()
            else:
                result=max(result,tomato[i][j][k])
print(result-1)
                
            
       



