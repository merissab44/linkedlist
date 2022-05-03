
def find_middle(head):
    left = head
    right = head
    while right and right.next:
        left = left.next
        right = right.next.next
    return left.data

# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
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