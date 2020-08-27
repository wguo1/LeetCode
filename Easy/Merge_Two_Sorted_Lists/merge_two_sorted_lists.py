# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nextNode = ListNode()
        head = nextNode
        while (l1 != None or l2 != None):
            if (not(l1)):
                nextNode.next = l2
                l2 = None
            elif(not(l2)):
                nextNode.next = l1
                l1 = None
            else:
                if (l1.val <= l2.val):
                    nextNode.next = l1
                    l1 = l1.next
                    nextNode = nextNode.next
                    nextNode.next = None
                else:
                    nextNode.next = l2
                    l2 = l2.next
                    nextNode = nextNode.next
                    nextNode.next = None
                    
        return head.next