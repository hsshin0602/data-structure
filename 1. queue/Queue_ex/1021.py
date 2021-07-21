from collections import deque
import sys

def put(q, data):
    return q.append(data)

def get(q):
    return q.popleft()

def rotate_left(q,n):
    return q.rotate(-1*n)

def rotate_right(q,n):
    return q.rotate(1*n)

def front(q):
    return q[0]
    
def qsize(q):
    return len(q)

q=deque()
N,M=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(1,N+1):
    put(q,i)
count=0
for i in range(M):
    if front(q)==arr[i]:
            get(q)
    else:
        cnt_left=q.index(arr[i])
        cnt_right=qsize(q)-q.index(arr[i])
        if cnt_right >= cnt_left:
            count+=cnt_left
            rotate_left(q, cnt_left)
            get(q)               
        elif cnt_right < cnt_left:
            count+=cnt_right
            rotate_right(q, cnt_right)
            get(q)
print(count)



