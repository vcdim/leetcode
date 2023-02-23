from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n-1
        val = nums[n-1]
        for i in range(n-2, -1, -1):
            c = nums[i]
            if c < val:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                nums = nums[:i+1] + sorted(nums[i+1:])
                return nums
        return nums.sort()