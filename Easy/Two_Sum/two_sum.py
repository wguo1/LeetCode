class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        index = 0
        for num in nums:
            if ((target - num) in results):
                return [results[target - num], index]
            else:
                results[num] = index
                index += 1
            
        return []