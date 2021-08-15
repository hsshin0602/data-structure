while True:
    n=int(input())
    if n==0:
        break
    cnt=0
    h=2*n+1
    prim=[True]*h
    for j in range(2,int(h**0.5+1)):
        if prim[j]==True:
            for k in range(j+j,h,j):
                prim[k]=False
    for i in range(n+1,2*n+1):
        if i>1 and prim[i]==True:
            cnt+=1
    print(cnt)
    