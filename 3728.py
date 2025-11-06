class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        if n < 3:
            return 0
      
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + capacity[i]
      
        ans = 0
        freq_map = defaultdict(int)
    
        l_val = capacity[0]
        p_l = prefix_sums[1]  # p[0]
        freq_map[(l_val, p_l)] += 1
    
        for r in range(2, n):
            r_val = capacity[r]
            p_r_minus_1 = prefix_sums[r]
            target_key = (r_val, p_r_minus_1 - r_val)
            ans += freq_map[target_key]
      
            l_val = capacity[r-1]
            p_l = prefix_sums[r] # p[r-1]
            key_to_store = (l_val, p_l)
            freq_map[key_to_store] += 1
      
        return ans