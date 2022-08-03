'''
Given the root of a binary tree
Return its maximum depth
    # max depth is number of nodes along the longest path from root down to farthest leaf
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    # base case: no left or right nodes return 1
    if root is None:
        return 0
    else:
        # Recursive case: the max of left/right branch 
        return 1 + max(max_depth(root.left), max_depth(root.right))


r = TreeNode(3)
l1 = TreeNode(9)
r1 = TreeNode(20)
r.left = l1
r.right = r1
r2l = TreeNode(15)
r2r = TreeNode(7)
r1.left = r2l
r1.right = r2r

print(max_depth(r))
