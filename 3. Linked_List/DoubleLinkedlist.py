from mynode import node
class myDoubleLinkedlist:
    def __init__(self):
        dummy=node(None)
        self.head=dummy
        self.tail=dummy

    def add(self, item):
        newNode=node(item)
        self.tail.next=newNode
        newNode.prev=self.tail
        self.tail=newNode

    def pop(self):
        delnode=self.tail
        self.tail=delnode.prev
        self.tail.next=None
        del delnode

    def delete(self, item):
        horse = self.head
        while horse.next:
            if horse.data == item:
                horse.prev.next = horse.next
                horse.next.prev = horse.prev
                del horse
                return
            horse = horse.next
        if horse.data == item: #item이 맨뒤에 있는경우
            horse.prev.next = None
            self.tail = horse.prev
            del horse
            return
    
    def getAll(self):               
        ret1 = []
        ret2 = []
        horse1 = self.head
        horse2 = self.tail
        # Double Linked List는 양방향으로 탐색할 수 있다.
        while horse1.next and horse2.prev and horse1 != horse2 and horse1.next != horse2:
            ret1.append(horse1.data)
            ret2.append(horse2.data)
            horse1 = horse1.next
            horse2 = horse2.prev

        if horse1 == horse2:
            ret1.append(horse1.data)
        else:
            ret1.append(horse1.data)
            ret2.append(horse2.data)
        ret = ret1[1:] + ret2[::-1]
        return ret 

dll = myDoubleLinkedlist()
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add(5)
dll.delete(4)
print(dll.getAll())                       # [1, 2, 3, 5]
dll.pop()
print(dll.getAll())                       # [1, 2, 3]
dll.delete(2)
print(dll.getAll())                       # [1, 3]
dll.pop()
print(dll.getAll())                       # [1]