# Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new **sorted** list. The new list should be made by splicing together the nodes of the first two lists.

#### Example:
```python
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```


### Answer Description
#### Author: William Guo
```python
n = number of nodes in l1 and l2
Asymptotic Runtime: O(n)
Memory: O(n)
```

Pretty simplistic algorithm of iterating through essentially both lists. Check which head is smaller and add it to the new list. Remove the smaller value and iterate to the next value. Keep a reference to the new head and return it.