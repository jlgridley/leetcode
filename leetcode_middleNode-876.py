class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    curr = head
    numNodes = 0
    while curr:
        numNodes += 1
        curr = curr.next
    curr = head
    idx = 0
    while idx < numNodes//2:
        curr = curr.next
        idx += 1
    return curr

vals = [1,2,3,4]
head = ListNode(1)
curr = head
for val in vals[1:]:
    curr.next = ListNode(val)
    curr = curr.next

curr = head
while curr:
    print(curr.val, end=' ')
    curr = curr.next
print()

print(middleNode(head).val)
