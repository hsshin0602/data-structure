import sys
from collections import deque

class node:
    def __init__(self,item):
        self.data=item
        self.left = None
        self.right = None

    def insert(self,item,l,r):
        if self.data != item:
            if self.left:
                self.left.insert(item, l, r)
            if self.right:
                self.right.insert(item, l, r)
        else:
            if l!='.':
                    self.left=node(l)
            if r!='.':
                    self.right=node(r)
    
    def inorder(self):
        ret=[]
        if self.left:
            ret+=self.left.inorder()
        ret+=[self.data]
        if self.right:
            ret+=self.right.inorder()
        return ret

    def preorder(self):
        ret=[]
        ret+=[self.data]
        if self.left:
            ret+=self.left.preorder()
        if self.right:
            ret+=self.right.preorder()
        return ret

    def postorder(self):
        ret=[]
        if self.left:
            ret+=self.left.postorder()
        if self.right:
            ret+=self.right.postorder()
        ret+=[self.data]
        return ret

class Tree:
    def __init__(self):
        self.root=None
    
    def insert(self,item,l,r):
        if self.root is None:
            self.root=node(item)
            if l!='.':
                self.root.left=node(l)
            if r!='.':    
                self.root.right=node(r)
        else:
            self.root.insert(item, l, r)
    def inorder(self):
        return self.root.inorder()
    def preorder(self):
        return self.root.preorder()
    def postorder(self):
        return self.root.postorder()

case=int(sys.stdin.readline())
bt=Tree()
for _ in range(case):
    arr=list(sys.stdin.readline().split())
    bt.insert(arr[0], arr[1], arr[2])  
  
a=bt.preorder()
b=bt.inorder()
c=bt.postorder()
    
print(''.join(a))
print(''.join(b))
print(''.join(c))