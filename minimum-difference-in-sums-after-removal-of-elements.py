import heapq

class Solution(object):
    def minimumDifference(self, nums):
       
        N = len(nums)
        n = N // 3

       
        prefix_min = [0] * N
        
        max_h = []
        current_sum = 0
        for i in range(N):
            num = nums[i]
            heapq.heappush(max_h, -num)
            current_sum += num
            
            if len(max_h) > n:
                
                current_sum += heapq.heappop(max_h)
            
            if len(max_h) == n:
                prefix_min[i] = current_sum

        
        suffix_max = [0] * N
        
        min_h = []
        current_sum = 0
        for i in range(N - 1, -1, -1):
            num = nums[i]
            heapq.heappush(min_h, num)
            current_sum += num
            
            if len(min_h) > n:
               
                current_sum -= heapq.heappop(min_h)

            if len(min_h) == n:
                suffix_max[i] = current_sum

        min_diff = float('inf')
        
        
        for p in range(n - 1, 2 * n):
            sum_first = prefix_min[p]
            sum_second = suffix_max[p + 1]
            min_diff = min(min_diff, sum_first - sum_second)

        return min_diff