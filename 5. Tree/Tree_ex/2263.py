import sys
sys.setrecursionlimit(10**9)

n=int(sys.stdin.readline())
inorder=list(map(int,sys.stdin.readline().split()))
postorder=list(map(int,sys.stdin.readline().split()))
in_location=[0 for _ in range(n+1)]

for i in range(n):
    in_location[inorder[i]]=i

def preorder(in_start,in_end,p_start,p_end):
    if in_start > in_end or p_start > p_end:
        return
    
    root=postorder[p_end]
    print(root,end=' ')
    left=in_location[root]-in_start
    right=in_end-in_location[root]

    preorder(in_start, in_start+left-1, p_start, p_start+left-1)
    preorder(in_end-right+1, in_end, p_end-right, p_end-1)

preorder(0, n-1,0,n-1)
