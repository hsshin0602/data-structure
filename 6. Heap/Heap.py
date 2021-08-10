class myheap:
    def __init__(self):
        self.arr=[None]

    def insert(self,item):
        self.arr.append(item)
        idx=len(self.arr)-1
        while idx > 1:
            if self.arr[idx] < self.arr[idx//2]: #부모노드를 찾을때 자식노드//2를 해준다
                self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
                idx//=2
            else:
                break

    def search(self, target):
        return self.arr.index(target)

    def delete(self, target):
        targetIDX=self.search(target)
        if targetIDX != len(self.arr)-1:
            self.arr[targetIDX]=self.arr.pop() #target idx위치에 마지막 값을 넣어서 다시 heap!
        else:
            self.arr.pop()
        for i in range(targetIDX,0,-1):
            self.maxHeapify(i)

    def maxHeapify(self,idx):
        left=2*idx #완전이진트리여서 왼쪽자식노드를 찾을때 *2를 해준다
        right=2*idx+1 #완전이진트리여서 오른자식노드를 찾을때 *2+1을 해준다
        parent=idx 

        if left < len(self.arr) and self.arr[idx] < self.arr[left]: #왼쪽자식이있는지 확인 + 크기비교
            parent=left

        if right < len(self.arr) and self.arr[idx] < self.arr[right]: #오른쪽자식이 있는지 확인 + 크기비교
            parent=right
        
        if parent != idx: # 배열값의 교환
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            self.maxHeapify(parent) # 바뀐 자식노드의 heap을 다시 재탐색

    def popRoot(self):
        ret=self.arr[1]
        self.arr[1]=self.arr.pop()
        self.maxHeapify(1)
        return ret
    
    def showAll(self):
        print(self.arr)

h = myheap()
h.insert(20); h.insert(4); h.insert(8);
h.insert(17); h.insert(15); h.insert(40);

h.showAll()
print(h.popRoot())
h.showAll()
h.delete(20)
h.showAll()

print(h.popRoot())