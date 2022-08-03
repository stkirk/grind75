'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''
import math
def middle_node(head):
    node_count = 0
    cur = head
    while cur:
        node_count += 1
        cur = cur.next
    mid = math.ceil((node_count + 1) / 2)
    cur = head
    for i in range(mid-1):
        cur = cur.next
    return cur
