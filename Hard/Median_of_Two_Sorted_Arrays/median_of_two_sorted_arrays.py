class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1) + len(nums2)
        even = (totalLength % 2 == 0)
        totalPos = 0
        median = 0
        
        if (even):
            medianList = [None, None]
            while (totalPos != (totalLength // 2) + 1):
                if (len(nums1) != 0 and len(nums2) != 0):
                    if (nums1[0] <= nums2[0]):
                        medianList.pop(0)
                        medianList.append(nums1.pop(0))
                    else:
                        medianList.pop(0)
                        medianList.append(nums2.pop(0))
                elif (len(nums1) == 0):
                    medianList.pop(0)
                    medianList.append(nums2.pop(0))
                else:
                    medianList.pop(0)
                    medianList.append(nums1.pop(0))
                    
                totalPos += 1
            
            median = (medianList[0] + medianList[1]) / 2
        else:
            while (totalPos != (totalLength // 2) + 1):
                if (len(nums1) != 0 and len(nums2) != 0):
                    if (nums1[0] <= nums2[0]):
                        median = nums1.pop(0)
                    else:
                        median = nums2.pop(0)
                elif (len(nums1) == 0):
                    median = nums2.pop(0)
                else:
                    median = nums1.pop(0)
                    
                totalPos += 1
                
        return median
        