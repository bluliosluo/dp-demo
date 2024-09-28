# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         sub = []
#         for num in nums:
#             i = bisect_left(sub, num)
#             if i == len(sub):
#                 sub.append(num)
#             else:
#                 sub[i] = num
#         return len(sub)
# Time: O(NlogN)
# Space: O(N)


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# Time: O(N^2)
# Space: O(N)