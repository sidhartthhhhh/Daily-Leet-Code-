class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        abs_nums = [abs(n) for n in nums]
    
        abs_nums.sort()
    
        score = 0
        n = len(nums)

        num_negative_terms = n // 2
    
        for i in range(num_negative_terms):
            score -= abs_nums[i] ** 2

        for i in range(num_negative_terms, n):
            score += abs_nums[i] ** 2
      
        return score