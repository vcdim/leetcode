from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        
        res = []
        for c in range(n-2):
            if c > 0 and nums[c] == nums[c-1]:
                continue
            l = c+1
            r = n-1
                
            while l < r:
                s = nums[c] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[c], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                elif s < 0:
                    l += 1
                else: 
                    r -= 1
        return res