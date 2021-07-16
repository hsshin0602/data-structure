#삽입은 막,꺼낼때 우선순위가 높은것을 먼저
#삽입은 put으로 순서대로 O(1), 탐색 및 삭제는 큰것을 선형탐색해서 O(N)
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
        else:
            priority=arg[0]
            item=arg[1]
            self.q.append([priority,item])

    def get(self):
        maxval = -1
        maxidx = -1
        if self.single:
            for idx, item in enumerate(self.q): # (0,q)식으로 인덱스의 번호와 같이 나오게 만듬
                if maxval < item:
                    maxval = item
                    maxidx = idx
            del self.q[maxidx]
            return maxval
        else:
            for idx, items in enumerate(self.q):
                if maxval < items[0]: # priority가[0]에 저장되어 있음
                    maxval = items[0]
                    maxitem = items[1]
                    maxidx = idx
            del self.q[maxidx]
            return [maxval, maxitem]

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