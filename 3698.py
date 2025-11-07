class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return -1
      
    # 1. Prefix Sum
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        total_sum = prefix_sum[n-1]
    
    # 2. Prefix Increasing Array
        inc = [False] * n
        inc[0] = True
        for i in range(1, n):
            if inc[i-1] and nums[i] > nums[i-1]:
                inc[i] = True
        
    # 3. Suffix Decreasing Array
        dec = [False] * n
        dec[n-1] = True
        for i in range(n-2, -1, -1): # Iterate from n-2 down to 0
            if dec[i+1] and nums[i] > nums[i+1]:
                dec[i] = True
        
    # 4. Find Minimum Difference
        min_diff = float('inf')
        found_valid_split = False
    
    # Iterate through all possible split points `i`
    # The split is between i and i+1
        for i in range(n - 1):
      # left = nums[0...i], right = nums[i+1...n-1]
            if inc[i] and dec[i+1]:
                found_valid_split = True
                sum_left = prefix_sum[i]
                sum_right = total_sum - sum_left
                min_diff = min(min_diff, abs(sum_left - sum_right))
        
    # 5. Return Result
        if not found_valid_split:
            return -1
        else:
            return min_diff