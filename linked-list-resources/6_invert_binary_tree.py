# given the root of a binary tree:
# invert the tree and return its root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Visit every node and look at its children, then swap them
def invert_tree(root):
    # Base Case:
    if root is None:
        return None
    # Recursive case
    else:
        # swap left/right
        root.left, root.right = root.right, root.left
        # run it on the children
        if root.right:
            invert_tree(root.right)
        if root.left:
            invert_tree(root.left)
        
        return root
            


test_root = TreeNode(4)
l1 = TreeNode(2)
r1 = TreeNode(7)
test_root.left = l1
test_root.right = r1
l2l = TreeNode(1)
l2r = TreeNode(3)
r2l = TreeNode(6)
r2r = TreeNode(9)
l1.left = l2l
l1.right = l2r
r1.left = r2l
r1.right = r2r
