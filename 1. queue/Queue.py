import queue
import random

q=queue.Queue() 
s=queue.LifoQueue() #stack과 같음
pq=queue.PriorityQueue()

for item in ['a','b','13','ss']:
    priority=random.randint(0,10)
    q.put(item) # queue에 data 삽입기능
    s.put(item)
    pq.put((priority, item))

def getList(data):
    size=data.qsize()
    ret=[]
    while size > 0:
        ret.append(data.get())#queue에 data를 pop하는 기능
        size=data.qsize()
    return ret

print(getList(q))
print(getList(s))
print(getList(pq))
