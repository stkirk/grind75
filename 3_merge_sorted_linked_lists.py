# Given the heads of 2 sorted linked lists
# merge the two lists into one sorted ll and return the head node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(start_node):
    node_list = []
    current_node = start_node
    while current_node:
        node_list.append(current_node.val)
        current_node = current_node.next
    print(node_list)

def merge_sorted_ll(list1, list2):
    # pointer for head of new list to be returned
    head = None
    # init pointers for current nodes from list1 and list 2, and new_list
    cur1 = list1
    cur2 = list2
    cur_new = ListNode()

    # while loop as long as BOTH lists have nodes
    while cur1 and cur2:
        if cur1.val <= cur2.val:
            if head is None:
                head = cur1
            # shuffle pointers
            cur_new.next = cur1
            cur_new = cur_new.next
            cur1 = cur1.next

        # else cur2.val > cur1.val or cur1 is None
        else:
            if head is None:
                head = cur2
            # shuffle pointers
            cur_new.next = cur2
            cur_new = cur_new.next
            cur2 = cur2.next

    # while loop end
    # add any remaing nodes or if one list or both were empty
    if cur1:
        if head is None:
            head = cur1
        cur_new.next = cur1
    if cur2:
        if head is None:
            head = cur2
        cur_new.next = cur2

    return head 

def merge_ll_recursive(list1, list2):
    # Base Case list1 or list2 are out of nodes or empty
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Recursive Case:
    if list1.val <= list2.val:
        list1.next = merge_ll_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_ll_recursive(list1, list2.next)
        return list2                                

#test cases
# list1 = 1->2->4
# list2 = 1->3->4
n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(4)
n2.next = n3

na = ListNode(1)
nb = ListNode(3)
na.next = nb
nc = ListNode(4)
nb.next = nc

# print_list(merge_ll_recursive(n1, na))
print_list(merge_sorted_ll(n1, na))
