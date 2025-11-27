class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # Count existing ones
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        # If gcd of entire array > 1 -> impossible
        overall = 0
        for x in nums:
            overall = gcd(overall, x)
        if overall != 1:
            return -1

        # Find shortest subarray with gcd == 1
        min_len = float('inf')
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = gcd(cur, nums[j])
                if cur == 1:
                    min_len = min(min_len, j - i + 1)
                    break  # no need to extend this start i further

        # min_len should be finite because overall gcd == 1
        # operations: (L-1) to create first 1 + (n-1) to spread it
        return (min_len - 1) + (n - 1)