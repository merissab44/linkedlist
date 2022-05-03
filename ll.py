
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

# Given a singly-linked list, find whether or not it contains a cycle, and if it does, find the node at which the cycle starts (the node that two other nodes reference/point to).
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