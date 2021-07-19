import sys
from collections import deque

class myqueue:
    def __init__(self):
        self.queue=deque()

    def put(self,data):
        self.queue.append(data)
    
    def get(self):
        return self.queue.popleft()
    def qsize(self):
        return len(self.queue)

    def rotate(self):
        self.queue.rotate(-1)

N=int(sys.stdin.readline().rstrip())
queue=myqueue()

for i in range(1,N+1):
    queue.put(i)
while queue.qsize() > 1:
    queue.get()
    queue.rotate()

print(queue.get())
