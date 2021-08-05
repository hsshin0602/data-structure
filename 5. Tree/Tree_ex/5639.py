import sys
sys.setrecursionlimit(10**6)

preorder=[]
while True:
    try:
        a=int(sys.stdin.readline())
        preorder.append(a)
    except:
        break
def postorder(start,end):
    if start > end:
        return
    if start == end:
        root=preorder[start]
        print(root)
        return

    root=preorder[start]
    right=0
    for i in range(start+1,end+1,1):
        if root < preorder[i]:
            right=int(i)
            break
    if right==0:
        left=end
        right=end+1
    else:
        left=right-1    
    postorder(start+1,left)
    postorder(right, end)
    print(root)

postorder(0,len(preorder)-1)