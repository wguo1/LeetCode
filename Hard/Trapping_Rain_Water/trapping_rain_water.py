class Solution:
    def trap(self, height: List[int]) -> int:
        def trapHelper(height: List[int]) -> int: 
            if (len(height) > 1):           
                total = 0
                curBeg = 0
                curEnd = len(height) - 1
                curPos = 1
                while (curPos < len(height)):
                    if (height[curBeg] <= height[curPos]):
                        total += (height[curBeg] * (curPos - curBeg))
                        curEnd = len(height) - 1
                        while (curBeg != curPos):
                            total -= height[curBeg]
                            curBeg += 1
                    else:
                        if (height[curPos] >= height[curEnd]):
                            curEnd = curPos
                        
                    curPos += 1  
                
                if (curEnd >= len(height)):
                    return total
                else:
                    curPos = curEnd
                    total += (height[curEnd] * (curEnd - curBeg))
                    while (curEnd > curBeg):
                        total -= height[curEnd]
                        curEnd -= 1
            
                    return total + trapHelper(height[curPos:])
            else:
                return 0
            
        return trapHelper(height)