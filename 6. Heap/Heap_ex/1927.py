import sys

class Heap:
    def __init__(self):
        self.arr=[None]

    def insert(self, item):
        self.arr.append(item)
        idx=len(self.arr)-1
        while idx >1:
            if self.arr[idx] < self.arr[idx//2]:
                self.arr[idx],self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
                idx=idx//2
            else:
                break

    def minHeapify(self,idx):
        parent=idx
        left=idx*2
        right=idx*2+1

        if left < len(self.arr) and self.arr[parent] > self.arr[left]:
            parent=left
        if right < len(self.arr) and self.arr[parent] > self.arr[right]:
            parent=right

        if parent != idx:
            self.arr[idx],self.arr[parent] = self.arr[parent],self.arr[idx]
            self.minHeapify(parent)

    def popRoot(self):
        if len(self.arr)==1:
            return 0
        else:
            if len(self.arr)==2:
                ret=self.arr.pop()
                return ret
            else:
                ret=self.arr[1]
                self.arr[1]=self.arr.pop()
                self.minHeapify(1)
                return ret

case=int(sys.stdin.readline())
heap=Heap()
for i in range(case):
    num=int(sys.stdin.readline())
    if num == 0:
        result=heap.popRoot()
        print(result)
    else:
        heap.insert(num)
                
'''
import heapq
import sys

case=int(sys.stdin.readline())
heap=[]

for _ in range(case):
    num=int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
'''
        


