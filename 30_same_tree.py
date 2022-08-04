'''
Given the roots of two binary trees, p and q:
    - if they are structurally identical
        # return True
        # if they aren't return False
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p,q):
    # init node_lists for p and q
    p_list = []
    q_list = []
    # write recursive DFS for a node to append to a list
    def dfs_append(root, node_list):
        # Base Case:
        if root is None:
            node_list.append(root)
        # Recursive Case:
        else:
            # append root.val to node_list
            node_list.append(root.val)
            # run dfs on root.right and root.left
            dfs_append(root.right, node_list)
            dfs_append(root.left, node_list)
    # run function on p and q
    dfs_append(p, p_list)
    dfs_append(q, q_list)
    # compare node_lists
    return p_list == q_list


p1 = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(3)
p1.left = l1
p1.right = r1

q1 = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(3)
q1.left = l1
q1.right = r1
print(is_same_tree(p1,q1)) # True

p2 = TreeNode(1)
l1 = TreeNode(2)
p2.left = l1

q2 = TreeNode(1)
r1 = TreeNode(2)
q2.right = r1
print(is_same_tree(p2,q2)) # False
