# 1. Two Sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have ***exactly*** one solution, and you may not use the *same* element twice.

#### Example:
```python
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```


### Answer Description
#### Author: William Guo
```python
n: length of nums
Asymptotic Runtime: O(n)
Memory: O(n)
```

Iterate through all numbers in nums. Subtract each option from the target and check to see if it is a key in the dictionary. If it works return a 2 element list otherwise store the number as a key and the index as a value.
