# Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

#### Example 1:
```python
Input: 123
Output: 321
```

#### Example 2:
```python
Input: -123
Output: -321

```

#### Example 3:
```python
Input: 120
Output: 21
```

##### Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


### Answer Description
#### Author: William Guo
```python
n: number of digits of x
Asymptotic Runtime: O(n)
Memory: O(n)
```

Check if x is negative. Then iterate through each digit and add it to a new number with the appropriate place value. Apply the negative sign after the iteration is done. Check if it is within the limits of a 32 bit integer. If it is not return 0.