import sys
from collections import deque

N=int(sys.stdin.readline())
graph=[]
for i in range(N):
    arr=list(map(int,sys.stdin.readline().rstrip()))
    graph.append(arr)

visit=[]
for _ in range(N):
    arr1=[[] for _ in range(N)]
    visit.append(arr1)

result=[]
for _ in range(N):
    arr2=[0 for _ in range(N)]
    result.append(arr2)

def BFS(a,b): # p는 튜플형식 (a,b)
    q=deque()
    q.append((a,b))
    result[a][b]=p
    group=[]
    group.append((a,b))
    while q:
        k,j=q.popleft() 
        for e,r in visit[k][j]:
            if result[e][r] == 0:
                result[e][r]=p
                group.append((e,r))
                q.append((e,r))
    return len(group) 


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            if (i,j) not in visit[i][j]: # 중요! 자기자신도 넣어주기 
                visit[i][j].append((i,j))
            if j+1 < N and graph[i][j+1]==1:
                if (i,j) not in visit[i][j+1]:
                    visit[i][j+1].append((i,j))
                if (i,j+1) not in visit[i][j]:
                    visit[i][j].append((i,j+1))

            if j-1 >= 0 and graph[i][j-1]==1:
                if (i,j) not in visit[i][j-1]:
                    visit[i][j-1].append((i,j))
                if (i,j-1) not in visit[i][j]:
                    visit[i][j].append((i,j-1))

            if i+1 < N and graph[i+1][j]==1:
                if (i,j) not in visit[i+1][j]:
                    visit[i+1][j].append((i,j))
                if (i+1,j) not in visit[i][j]:
                    visit[i][j].append((i+1,j))

            if i-1 >= 0 and graph[i-1][j]==1:
                if (i,j) not in visit[i-1][j]:
                    visit[i-1][j].append((i,j))
                if (i-1,j) not in visit[i][j]:
                    visit[i][j].append((i-1,j))
            
p=0
l=[]
for i in range(N):
    for j in range(N):
        if visit[i][j] and result[i][j] == 0:
            p+=1
            u=BFS(i,j)
            l.append(u)

print(p)
l=sorted(l)
for i in range(len(l)):
    print(l[i])