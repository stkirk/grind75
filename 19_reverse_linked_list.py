# given the head of a singly linked list
# reverse the list and return the new head

# Print linked list
def print_list(start_node):
    node_list = []
    current_node = start_node
    while current_node:
        node_list.append(current_node.val)
        current_node = current_node.next
    print(node_list)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_sll(head):
    if head == None or head.next == None:
        return head
    
    cur = head
    new_next = None
    # while loop starting at head
    while cur:
        temp = cur.next
        cur.next = new_next
        new_next = cur
        cur = temp

    return new_next

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
n5 = ListNode(5)
n4.next = n5

print_list(reverse_sll(n1)) # [5,4,3,2,1]
print_list(reverse_sll(None)) # []
print_list(reverse_sll(n4)) # [5,4]
