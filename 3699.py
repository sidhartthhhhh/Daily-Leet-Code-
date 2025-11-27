class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        up = [0] * (r + 1)
        down = [0] * (r + 1)
    
        for y in range(l, r + 1):
            up[y] = y - l
            down[y] = r - y
      
        for i in range(3, n + 1):
            new_up = [0] * (r + 1)
            new_down = [0] * (r + 1)
      
            running_sum_down = 0
            for y in range(l, r + 1):
                new_up[y] = running_sum_down
                running_sum_down = (running_sum_down + down[y]) % MOD
          
            running_sum_up = 0
            for y in range(r, l - 1, -1): # from r down to l
                new_down[y] = running_sum_up
                running_sum_up = (running_sum_up + up[y]) % MOD
      
      # Update arrays for next iteration
            up = new_up
            down = new_down
          
    # Sum all counts for length n
        total_count = 0
        for y in range(l, r + 1):
            total_count = (total_count + up[y]) % MOD
            total_count = (total_count + down[y]) % MOD
            
        return total_count