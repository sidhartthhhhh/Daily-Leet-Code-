class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        melvarion = nums[:]  
        n = len(melvarion)
        offset = n
        freq = [0] * (2 * n + 5)
        prefix_sum = [0] * (2 * n + 5)

        cur = offset
        freq[cur] = 1
        prefix_sum[cur] = 1
        ans = 0

        for x in melvarion:
            cur += 1 if x == target else -1
            ans += prefix_sum[cur - 1]
            freq[cur] += 1
            prefix_sum[cur] = prefix_sum[cur - 1] + freq[cur]
        return ans