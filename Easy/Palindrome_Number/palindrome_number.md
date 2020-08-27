# 9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

#### Example 1:
```python
Input: 121
Output: true
```

#### Example 2:
```python
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

#### Example 3:
```python
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

##### Follow up:
Coud you solve it without converting the integer to a string?



### Answer Description
#### Author: William Guo
```python
n = number of digits in x
Asymptotic Runtime: O(log(n))
Memory: O(n)
```

Use a helper function for recursion. Convert it to a string and checks if the first and last characters are equal. Recursivly iterate until there is only one digit left or until there isn't a palindrome. There is a function without conversion as stated by the follow up prompt in the comments.
