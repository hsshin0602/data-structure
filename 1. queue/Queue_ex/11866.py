import sys
from collections import deque

class myqueue:
    def __init__(self):
        self.queue=deque()
    def put(self,data):
        self.queue.append(data)

    def get(self):
        return self.queue.popleft()

    def rotate(self):
        self.queue.rotate(-(K-1))

    def qsize(self):
        return len(self.queue)
    def getlist(self):
        return self.queue

N,K=map(int,sys.stdin.readline().rstrip().split())
queue=myqueue()
result=[]
for i in range(1,N+1):
    queue.put(i)

while queue.qsize() != 0:
    queue.rotate()
    result.append(queue.get())

print('<', end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print('>',end='')
    
