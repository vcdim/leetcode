from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, u in enumerate(nums):
            if u in m:
                return [m[u], i]
            m[target - u] = i
        return []