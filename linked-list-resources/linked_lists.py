# ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Print linked list
def print_list(start_node):
    node_list = []
    current_node = start_node
    while current_node:
        node_list.append(current_node.val)
        current_node = current_node.next
    print(node_list)