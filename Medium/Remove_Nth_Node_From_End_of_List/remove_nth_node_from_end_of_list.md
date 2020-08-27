# 19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

#### Example 1:
```python
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

##### Note:
Given n will always be valid.

##### Follow Up:
Could you do this in one pass?

### Answer Description
#### Author: William Guo
```python
x = length of linked list
Asymptotic Runtime: O(x)
Memory: O(size of node * (n + 1))
```

Store n + 1 nodes in a temporary list. This will keep storing until it gets to the end of the list. There are n nodes for the end of the list as well as one previous to connect to once the link is broken. Then there are a couple of edge cases when the element being removed is the first element or when there are only 2 elements in the list.
