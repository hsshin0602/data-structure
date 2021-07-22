import sys

def push(st,data):
    return st.append(data)
def pop(st):
    return st.pop() if st else -1
def size(st):
    return len(st)
def empty(st):
    return 1 if not st else 0
def top(st):
    return st[-1] if st else -1

st=[]
case=int(sys.stdin.readline())
for i in range(case):
    order=sys.stdin.readline().rstrip().split()
    cmd=order[0]
    if order[0] == 'push':
        push(st,order[1])
    elif order[0] == 'pop':
        sys.stdout.write(str(pop(st)) + '\n')
    elif order[0] == 'size':
        sys.stdout.write(str(size(st)) + '\n')
    elif order[0] == 'top':
        sys.stdout.write(str(top(st)) + '\n')
    elif order[0] == 'empty':
        sys.stdout.write(str(empty(st)) + '\n')