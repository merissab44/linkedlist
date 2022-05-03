
def find_middle(head):
    left = head
    right = head
    while right and right.next:
        left = left.next
        right = right.next.next
    return left.data