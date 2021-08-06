import sys
from collections import deque
import math

def tree_search(tree):
    q=deque()
    arr=[]
    cnt=0
    sum=0
    q.append(tree[0])
    arr.append(tree[0])
    visit[q[0]]=1
    while q:
        front=q.popleft()
        for j in graph[front]:
            if visit[j]==0:
                visit[j]=1
                q.append(j)
                arr.append(j)  
    if arr == tree: #만들어질 트리가 하나
        for i in arr:
            sum+=len(graph[i]) #간선의 개수
        if len(arr)-1 == math.ceil(sum/2): #트리의 조건
            cnt+=1
            tree.clear()
            return cnt,tree
        else:
            tree.clear()
            return cnt,tree
    else: # 만들어질 트리가 여러개
        for i in arr:
            sum+=len(graph[i])
        if len(arr)-1 == math.ceil(sum/2):
            cnt+=1
            tree=[x for x in tree if x not in arr]
            return cnt,tree
        else:
            tree=[x for x in tree if x not in arr]
            return cnt,tree

case=0
while True:
    n,m=map(int,sys.stdin.readline().split())
    if not n and not m:
        break
    graph=[[] for _ in range(n+1)]
    visit=[0 for i in range(n+1)]
    case+=1 
    cnt_tree=0
    tree=[]
    for i in range(1,m+1):
        a,b=map(int,sys.stdin.readline().split())
        if not a in tree:
            tree.append(a)
        if not b in tree: 
            tree.append(b)
        graph[a].append(b)
        graph[b].append(a)
    
    cnt_tree += n-len(tree)
    while tree:
        cnt,tree=tree_search(tree)
        cnt_tree+=cnt
        
    if cnt_tree==0:
        print('Case %d: No trees.' %case)
    if cnt_tree==1:
        print('Case %d: There is one tree.' %case)
    elif cnt_tree > 1:
        print('Case %d: A forest of %d trees.'%(case,cnt_tree))
