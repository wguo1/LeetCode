# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if (not(n)):
            return head
        
        nodes = []
        nOld = n
        n += 1
        count = 0
        newHead = head
        
        while (head != None):
            if (n != 0):
                nodes = nodes + [head]
                n -= 1
            else:
                nodes = nodes[1:] + [head]
                
            head = head.next
            count += 1
        
        if (nOld == count):
            newHead = newHead.next
        elif (len(nodes) == 2):
            nodes[0].next = None
        else:
            nodes[0].next = nodes[2]
            
        return newHead