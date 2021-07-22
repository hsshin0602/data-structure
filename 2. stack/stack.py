class myStack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        return self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

stack=myStack()
for i in range(10):
    stack.push(i)

while stack.size():
    print(stack.pop(), end=' ')