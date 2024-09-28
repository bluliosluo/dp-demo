from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = nums[0]
        max_res = nums[0]
        for num in nums[1:]:
            max_ending = max(max_ending + num, num)
            max_res = max(max_res, max_ending)
        return max_res
