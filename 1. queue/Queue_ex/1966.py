import sys
from collections import deque

testcase = int(sys.stdin.readline().rstrip())
for _ in range(testcase):
    N,M=map(int,sys.stdin.readline().strip().split())
    q=deque(map(int, sys.stdin.readline().rstrip().split()))
    idx=deque(list(range(N)))
    cnt=0
    while q:
        max_q=max(q)
        if max_q == q[0]:
            cnt+=1
            q.popleft()
            if idx.popleft()==M:
                print(cnt)
                break
        else:
            q.rotate(-1)
            idx.rotate(-1)

  

    


