import sys
A=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
stack=[]
result=[-1 for _ in range(A)]
for i in range(A):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()]=arr[i]
    stack.append(i)
for i in result: #print(*result)
    print(i,end=' ')