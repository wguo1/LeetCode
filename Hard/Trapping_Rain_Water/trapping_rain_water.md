# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
*The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!*

#### Example:
```python
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

### Answer Description
#### Author: William Guo
```python
n = length of height
Asymptotic Runtime: O(n)
Memory: O(1)
```

Use a helper function for recursion. Broke elavation down into localized maxes. When encountering a column check to see if it is bigger than the current max. If it is then we can compute the water trapped in the "bowl" shape. Otherwise check at the end if there is a smaller max that represent one end of the bowl and our current max which represents the other side. Add it all together by first adding a rectangular shape of the length between maxes multiplied by the smaller max. Then subtract it by the height of each column inbetween.
