from collections import deque
import sys

def put(q,data):
    return q.append(data)

def getAll(q):
    ret=[]
    for i in q:
        ret.append(i)
    print('[' + ",".join(ret) + ']')

T=int(sys.stdin.readline())
for i in range(T):
    p=sys.stdin.readline().rstrip()
    case=int(sys.stdin.readline())
    arr=sys.stdin.readline()[1:-2].split(',') #중요
    q=deque()
    for i in range(len(arr)):
        put(q, arr[i])
    reverse = 0 # false
    error = 0 # True
    for i in p:
        if i=='R':
            if reverse == 0:
                reverse = 1
            else:
                reverse = 0
        else: # i==D
            if q and q[0] != '':
                if reverse == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                error = 1
                break
    if error == 1: 
        print("error")
    else:
        if reverse == 1: 
            q.reverse()  
        getAll(q)
    
