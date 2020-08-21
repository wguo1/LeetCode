import re
class Solution:
    def myAtoi(self, str: str) -> int:
        pat = re.compile(r"\A[ ]*([+-]?\d+)")
        match = pat.search(str)
        
        if (match):
            result = int(match.group(1))
            
            if ((-1 << 31) < result < (1 << 31) - 1):
                return result
            elif (result > 0):
                return (1 << 31) - 1
            else:
                return (-1 << 31)
        
        return 0