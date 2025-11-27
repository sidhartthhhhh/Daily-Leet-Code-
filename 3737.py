class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        dresaniel = nums[:]
        
        for i in range(n):
            target_count = 0
            for j in range(i, n):
                if dresaniel[j] == target:
                    target_count += 1
                length = j - i + 1
                if target_count > length // 2:
                    count += 1
        return count