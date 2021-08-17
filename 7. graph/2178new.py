from collections import deque
import sys

N,M=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(x,y):
    arr=[]
    graph[x][y]='#'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny]==1:
                graph[nx][ny]='#'
                arr.append((nx,ny))
    return arr

q=deque()
q.append((0,0))
cnt=0
while q:
    for _ in range(len(q)):
        x,y=q.popleft()
        for arr in BFS(x, y):
            q.append(arr)
    cnt+=1
    if (N-1,M-1) in q:
        cnt+=1 #마지막 한개만 남았다는 뜻
        print(cnt)
        exit()

print(cnt)

