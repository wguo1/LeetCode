# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if (len(lists) > 2):
            lists = [self.mergeKLists(lists[:len(lists) // 2]), 
                     self.mergeKLists(lists[len(lists) // 2:])]
        
        if (not(len(lists))):
            return None
        else:
            l1 = lists[0]
            l2 = None
            if (len(lists) == 2):
                l2 = lists[1]
                
            def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode: 
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
            
            return mergeTwoLists(l1, l2)
        