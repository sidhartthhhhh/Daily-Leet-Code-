class Solution(object):
    def maximumLength(self, nums, k):
        n = len(nums)
        max_len = 1

        for val in range(k):  
            dp = [0] * k  
            for num in nums:
                rem = num % k
                need = (val - rem + k) % k
                dp[rem] = max(dp[rem], dp[need] + 1)
                max_len = max(max_len, dp[rem])

        return max_len