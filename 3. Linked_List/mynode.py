class node:
    def __init__(self,item):
        self.data=item
        self.next=None
        self.prev=None

    def setData(self,item):
        self.data=item

    def setNext(self, target):
        self.next=target