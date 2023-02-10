from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            res = []
            
            if not nums:
                return res
            
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res
        
        def twoSum(nums, target):
            res = []
            n = len(nums)
            l = 0
            r = n-1
            
            while (l < r):
                s = nums[l] + nums[r]
                if s < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                elif s > target or (r < n-1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)