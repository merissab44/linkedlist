
# create node class
from heapq import merge


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAfter(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def deleteNodeAtPos(self, pos):
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def deleteList(self):
        temp = self.head
        while temp:
            prev = temp.next
            del temp.data
            temp = prev

def find_middle(head):
    left = head
    right = head
    while right and right.next:
        left = left.next
        right = right.next.next
    return left.data

def merge_sorted(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data < head2.data:
        head1.next = merge_sorted(head1.next, head2)
        return head1
    else:
        head2.next = merge_sorted(head1, head2.next)
        return head2

def find_cycle(head):
    if not head:
        return None
    if not head.next:
        return None
    if not head.next.next:
        return None
    left = head
    right = head
    while right and right.next:
        left = left.next
        right = right.next.next
        if left == right:
            break
    if not right or not right.next:
        return None
    left = head
    while left != right:
        left = left.next
        right = right.next
    return left

def kth_to_last(head, k):
    if not head:
        return None
    if not head.next:
        return head.data
    left = head
    right = head
    for i in range(k):
        right = right.next
        if not right:
            return None
    while right:
        left = left.next
        right = right.next
    return left.data


def rearrange_ll(head):
    if not head: return []
    left, right = head, head
    while right.next and right.next.next:
        left = left.next
        right = right.next.next
        
    prev, curr = None, left.next
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node    
    left.next = None
        
    head1, head2 = head, prev
    while head2:
        next_node = head1.next
        head1.next = head2
        head1 = head2
        head2 = next_node

    