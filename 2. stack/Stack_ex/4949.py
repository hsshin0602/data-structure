import sys
def top(st):
    return st[-1]
while True:
    arr=sys.stdin.readline().rstrip()
    st=[]
    nonflag=0
    if arr== '.':
        break       
    for i in arr:
        if i == '(' or i == '[':
            st.append(i)
        elif i == ')':
            if st and top(st)=='(':
                st.pop()
            else:
                nonflag=1
                break
        elif i == ']':
            if st and top(st)=='[':
                st.pop()
            else:
                nonflag=1
                break
    if nonflag==0 and not(st):
        print('yes')
    else:
        print('no')
    