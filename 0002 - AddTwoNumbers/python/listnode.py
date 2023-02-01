class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyList:
    def __init__(self, vals):
        self.head = ListNode(vals[0])

        currentNode = self.head
        for u in vals[1:]:
            currentNode.next = ListNode(u)
            currentNode = currentNode.next