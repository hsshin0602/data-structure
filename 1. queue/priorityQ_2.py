#삽입할때 우선순위대로 정렬, 꺼낼때 바로 꺼냄
#삽입은 sort수행으로 O(N lg N), 탐색 및 삭제는 popleft로 바로 꺼내서 O(1)
from collections import deque
import random

class priorityQ:
    single=False
    def __init__(self):
        self.q=deque()

    def put(self,*arg): # 몇개인지 모르기에 arg 주소로 알려주기 위해서 
        if len(arg)==1: #priority와 item이 같이 있는건지 비교
            self.single=True

        if self.single:
            priority=arg[0]
            self.q.append(priority)
            self.q=deque(sorted(self.q,reverse=True)) #내림차순
        else:
            priority=arg[0]
            item=arg[1]
            self.q.append([priority,item])
            self.q=deque(sorted(self.q, key = lambda x: x[0],reverse=True)) # 우선순위값(key)을 기준으로 내림차순

    def get(self):
        return self.q.popleft()

    def qsize(self):
        return len(self.q)

    def getAll(self):
        ret=[]
        while self.qsize() > 0:
            ret.append(self.get())
        self.single=False
        return ret

mq=priorityQ()

for item in ['a','b',13,'ss']:
    priority=random.randint(0,10)
    mq.put(priority,item)

print(mq.getAll())

for item in [1,5,2,4,3]:
    mq.put(item)

print(mq.getAll())