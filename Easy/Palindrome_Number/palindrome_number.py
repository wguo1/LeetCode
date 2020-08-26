class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            def isPalinHelper(y: str) -> bool:
                if (len(y) > 1):
                    return y[0] == y[-1] and isPalinHelper(y[1:-1])
                else:
                    return True
            
            return isPalinHelper(str(x))
        else:
            return False

#class Solution:
#    def isPalindrome(self, x: int) -> bool:
#        if (x < 0):
#            return False
#       else:
#            result = x
#            tester = 0
#            while (tester < x):
#                if (result):
#                    tester = (tester * 10) + (result % 10)
#                    result //= 10
#                else:
#                    return False
#            
#            return tester == x