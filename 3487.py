class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set(nums)
        max_val = max(nums)

        if max_val < 0:
            return max_val

        return sum(x for x in unique if x >= 0)