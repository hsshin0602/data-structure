from collections import deque
import sys

def push_front(queue,data):
    return queue.appendleft(data)

def push_back(queue,data):
    return queue.append(data)

def pop_front(queue):
    return queue.popleft() if queue else -1

def pop_back(queue):
    return queue.pop() if queue else -1

def size(queue):
    return len(queue)

def empty(queue):
    return 0 if queue else 1

def front(qeque):
    return queue[0] if queue else -1

def back(qeque):
    return queue[-1] if queue else -1

queue=deque()
num=int(sys.stdin.readline().rstrip())
for _ in range(num):
    command=list(sys.stdin.readline().rstrip().split())
    order=command[0]
    if order == "push_front":
        push_front(queue,command[1])
    elif order == "push_back":
        push_back(queue,command[1])
    elif order == "pop_front":
        sys.stdout.write(str(pop_front(queue))+ "\n")
    elif order == "pop_back":
        sys.stdout.write(str(pop_back(queue))+ "\n")
    elif order == "size":
        sys.stdout.write(str(size(queue)) + "\n")
    elif order == "empty":
        sys.stdout.write(str(empty(queue))+ "\n")
    elif order == "front":
        sys.stdout.write(str(front(queue))+ "\n")
    elif order == "back":
        sys.stdout.write(str(back(queue))+ "\n")
