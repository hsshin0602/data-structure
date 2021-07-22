import sys
K=int(sys.stdin.readline())
st=[]
for i in range(K):
    order=int(sys.stdin.readline())
    if order !=0:
        st.append(order)
    else:
        st.pop()
if st:
    print(sum(st))
else:
    print('0')