import sys

case = int(sys.stdin.readline())
order=[]
for i in range(case):
    cmd=int(sys.stdin.readline().rstrip())
    order.append(cmd)
arr=sorted(order)
good=[]
a=[]
k=0
for i in order:
    while k<len(arr)+1:
        if good:
            if good[-1]!=i:
                if k==len(arr):
                    print('NO')
                    exit()
                else:  
                    good.append(arr[k])
                    a.append('+')
                k+=1
            else:
                good.pop()
                a.append('-')
                break
        else:
            good.append(arr[k])
            a.append('+')
            k+=1

print('\n'.join(a))


    
