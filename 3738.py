class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        serathion = nums[:]
        left = [1] * n
        for i in range(1, n):
            if serathion[i] >= serathion[i - 1]:
                left[i] = left[i - 1] + 1
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if serathion[i] <= serathion[i + 1]:
                right[i] = right[i + 1] + 1
        ans = max(left)
        for i in range(n):
            l = left[i - 1] if i > 0 else 0
            r = right[i + 1] if i < n - 1 else 0
            if 0 < i < n - 1 and serathion[i - 1] <= serathion[i + 1]:
                ans = max(ans, l + 1 + r)
            else:
                ans = max(ans, max(l, r) + 1)
        return min(ans, n)