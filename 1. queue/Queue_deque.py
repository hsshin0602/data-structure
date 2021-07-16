#list로 구현 가능하지만 시간복잡도가 O(n),deque는 O(1)데크
'''
deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
deque.remove(item): item을 데크에서 찾아 삭제한다.
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
'''
from collections import deque
import queue

class myQueue:
    def __init__(self):
        self.q=deque()
    def put(self,data):
        self.q.append(data)
    def get(self,data):
        self.q.popleft(data) #선입선출
    def qsize(self):
        return len(self.q)
    def getList(self):
        return self.q

mq=myQueue()

for data in ['a','b',13,'ss']:
    mq.put(data)

print(mq.getList())
