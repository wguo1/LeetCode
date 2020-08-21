class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        
        index = 0
        newStrings = dict.fromkeys(range(numRows), "")
        newStr = ""
        
        for c in s:
            newStrings[abs(index)] = newStrings[abs(index)] + c
            
            if (index == numRows - 1):
                index *= -1
                
            index += 1
                
        for line in newStrings.values():
            newStr = newStr + line
            
        return newStr