class node:
    def __init__(self,item=-1):
        self.data=item
        self.left=None
        self.right=None

    def insert(self, item):
        if self.data > item:
            if self.left:
                self.left.insert(item) #self.left=insert(self.left,item)
            else:
                self.left=node(item)
        elif self.data < item:
            if self.right:
                self.right.insert(item)
            else:
                self.right=node(item)
        else: # self.data==item
            raise KeyError('Item is already exist!' % item)

    def inorder(self): #self=root
        ret=[]
        if self.left: 
            ret+=self.left.inorder()
        ret+=[self.data]
        if self.right: 
            ret+=self.right.inorder()
        return ret

    def height(self):
        l,r = 0, 0
        if self.left:
            l=self.left.height()
        if self.right:
            r=self.right.height()
        return max(l,r)+1

    def size(self):
        l, r = 0, 0
        if self.left:
            l=self.left.size()
        if self.right:
            r=self.right.size()
        return l+r+1

    def search(self, target, parent=None):
        if self.data==target: # =root의 data
            return self,parent
        elif self.data > target:
            if self.left:
                return self.left.search(target,self)
        else:
            if self.right:
                return self.right.search(target,self)

class myBinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self, item):
        if self.root is None:
            self.root=node(item)
        else:
            self.root.insert(item)

    def inorder(self):
        return self.root.inorder()

    def height(self):
        return self.root.height()

    def size(self):
        return self.root.height()

    def search(self, target):
        return self.root.search(target)

    def delete(self, target):
        targetNode, targetParent = self.root.search(target)
        # 삭제할 node가 자식이 모두 없는 경우
        if targetNode.left is None and targetNode.right is None:
            if targetNode.data < targetParent.data:
                targetParent.left = None
            else:
                targetParent.right = None
            del targetNode

        # 삭제할 node가 오른쪽 자식만 있는 경우
        elif targetNode.left is None:
            if targetNode.data < targetParent.data:
                targetParent.left = targetNode.right
            else:
                targetParent.right = targetNode.right
            del targetNode

        # 삭제할 node가 왼쪽 자식만 있는 경우
        elif targetNode.right is None:
            if targetNode.data < targetParent.data:
                targetParent.left = targetNode.left
            else:
                targetParent.right = targetNode.left
            del targetNode

        # 삭제할 node가 자식이 둘 다 있는 경우 
        else:
            horse = targetNode.left
            # 대신 삭제될 node(horse)의 부모가 원래 삭제될 node(targetNode)인 경우
            if horse.right is None:
                targetNode.data = horse.data
                targetNode.left = horse.left
                del horse
            
            # targetNode 보다 작은 가장 큰 값을 찾는 과정
            else:
                turtle = targetNode
                while horse.right:
                    turtle = horse
                    horse = horse.right
                    
                targetNode.data = horse.data
                turtle.right = None
                del horse
bt = myBinarySearchTree()

print("10, 4, 20, 1, 24, 7 삽입")
bt.insert(10);bt.insert(4);bt.insert(20)
bt.insert(1);bt.insert(24);bt.insert(7)
print(bt.inorder())

print("10 삭제")
bt.delete(10)
print(bt.inorder())

print("4 삭제")
bt.delete(4)
print(bt.inorder())

print("3, 5, 444, 445 삽입")
bt.insert(3);bt.insert(5)
bt.insert(444);bt.insert(445)
print(bt.inorder())