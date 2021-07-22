import sys
case=int(sys.stdin.readline())
for i in range(case):
    arr=sys.stdin.readline().rstrip()
    st=[]
    for j in arr:
        if j=='(':
            st.append(j)
        else: # ')'
            if '(' in st:
                st.pop()
            else:
                st.append(j)
    if st:
        print('NO')
    else:
        print('YES')
        