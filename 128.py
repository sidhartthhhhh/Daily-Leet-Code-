class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_streak = 0
        for num in num_set:
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                max_streak = max(max_streak, current_streak)
                
        return max_streak