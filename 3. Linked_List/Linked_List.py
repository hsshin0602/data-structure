from mynode import node

class myLinkedList:
    def __init__(self):
        dummy=node(None)
        self.head=dummy

    def add(self, item):
        newNode=node(item)
        horse=self.head
        while horse.next:
            horse=horse.next
        horse.next=newNode

    def pop(self):
        horse=self.head
        turtle=self.head
        while horse.next:
            target=horse
            horse=horse.next
        ret=horse.data
        turtle.next=None
        return ret

    def delete(self,item):
        horse=self.head
        turtle=self.head
        while horse.next:
            if horse.data == item:
                turtle.next=horse.next
                del horse
                return
            turtle=horse
            horse=horse.next
        if horse.data == item: # item이 맨뒤에 있는경우
            turtle.next=horse.next
            del horse
            return

    def getAll(self):
        ret=[]
        horse=self.head
        while horse.next:
            ret.append(horse.data)
            horse=horse.next
        ret.append(horse.data)
        return ret[1:]

ll = myLinkedList()
ll.add(1)               # 노드 1 리스트에 추가 
ll.add(2)               # 노드 2 리스트에 추가 
ll.add(3)               # 노드 3 리스트에 추가 
print(ll.getAll())      # 1 2 3 출력 
ll.delete(2)            # 노드 2 삭제 
print(ll.getAll())      # 1 3 출력 
ll.delete(1)            # 노드 1 삭제 
print(ll.getAll())      # 3 출력 
ll.delete(3)            # 노드 3 삭제 

