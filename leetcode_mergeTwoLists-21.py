def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1
    curr1 = list1
    curr2 = list2
    if list2.val <= list1.val:
        newHead = list2
        prev = list2
        curr2 = curr2.next
    else:
        newHead = list1
        prev = list1
        curr1 = curr1.next
    while curr1 or curr2:
        if not curr1 or (curr2 and curr2.val < curr1.val):
            prev.next = curr2
            curr2 = curr2.next
        elif not curr2 or (curr1 and curr1.val <= curr2.val):
            prev.next = curr1
            curr1 = curr1.next
        prev = prev.next
    return newHead
