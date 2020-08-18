# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = 0
        return_list = ListNode()
        beg_list = return_list
        while (l1 != None or l2 != None):
            if (l1 != None and l2 != None):
                total += (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
            elif (l1 != None):
                total += l1.val
                l1 = l1.next
            else:
                total += l2.val
                l2 = l2.next
                
            return_list.val = total % 10
            total //= 10
            if (l1 != None or l2 != None):
                return_list.next = ListNode()
                return_list = return_list.next
                
        if (total != 0):
            return_list.next = ListNode()
            return_list.next.val = total
        
        return beg_list