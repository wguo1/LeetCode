# Median of Two Sorted Arrays

There are two sorted arrays `nums1` and `nums2` of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume `nums1` and `nums2` cannot be both empty.

#### Example 1:
```python
nums1 = [1, 3]
nums2 = [2]
```

#### Example 2:
```python
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```


### Answer Description
#### Author: William Guo
```python
n = length of nums1
m = length of nums2
Asymptotic Runtime: O(log(m+n))
Memory: O(1)
```

Iterate until half of the numbers have been accounted for. Check the front of each list and compare. The smaller one will be the current median if the total size is odd. Otherwise if it is of even size then store it in a 2 element list but remove the smallest element of the three. Regardless remove the smallest element of both lists and iterate through.