# Merge k Sorted Lists

Given an array of linked-lists lists, each linked list is sorted in ascending order.

Merge all the linked-lists into one sort linked-list and return it.

#### Example 1:
```python
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

#### Example 2:
```python
Input: lists = []
Output: []
```

#### Example 2:
```python
Input: lists = [[]]
Output: []
```

#### Constraints:
* ```k == lists.length```
* ```0 <= k <= 10^4```
* ```0 <= lists[i].length <= 500```
* ```-10^4 <= lists[i][j] <= 10^4```
* ```lists[i]``` is sorted in **ascending order**.
* The sum of ```lists[i].length``` won't exceed ```10^4```.


### Answer Description
#### Author: William Guo
```python
x = length of lists
y = length of all elements of lists added together
n = number of nodes in l1 and l2
Asymptotic Runtime: O(log(x) * n)
Memory: O(log(x) * y)
```

Use a merge sort concept in answering this question. Split lists into sub operations where each recursive operation will only act when there are 2 or less elements. Then use a preexisting function from xyz to perform the actual sorting operation.