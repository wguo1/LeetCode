class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg = (x < 0)
        if (neg):
            x *= -1
        
        while (x != 0):
            rev *= 10
            rev += x % 10
            x //= 10
        
        if (neg):
            rev *= -1
        
        if (rev < ((1 << 31) - 1) and rev > (-1 << 31)):
            return rev
        else:
            return 0