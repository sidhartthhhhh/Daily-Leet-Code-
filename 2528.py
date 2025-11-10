class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        
        initial_power = [0] * n
        power_diff = [0] * (n + 1)
        
        for i in range(n):
            if stations[i] == 0:
                continue
            start = max(0, i - r)
            end = min(n - 1, i + r)
            power_diff[start] += stations[i]
            if end + 1 <= n:
                power_diff[end + 1] -= stations[i]
        
        current_power_sum = 0
        min_initial = float('inf')
        max_initial = 0
        for i in range(n):
            current_power_sum += power_diff[i]
            initial_power[i] = current_power_sum
            min_initial = min(min_initial, initial_power[i])
            max_initial = max(max_initial, initial_power[i])

        def check(target_power):
            stations_used = 0
            add_diff = [0] * (n + 1)
            current_added_power = 0
            
            for i in range(n):
                current_added_power += add_diff[i]
                total_power_i = initial_power[i] + current_added_power
                
                if total_power_i < target_power:
                    needed = target_power - total_power_i
                    stations_used += needed
                    
                    if stations_used > k:
                        return False
                        
                    current_added_power += needed
                    
                    j = min(n - 1, i + r)
                    end_index = min(n - 1, j + r)
                    stop_index = end_index + 1
                    
                    if stop_index <= n:
                        add_diff[stop_index] -= needed
            return True
        low = min_initial
        high = max_initial + k
        ans = low
        
        while low <= high:
            mid_target = (low + high) // 2
            if check(mid_target):
                ans = mid_target 
                low = mid_target + 1
            else:
                high = mid_target - 1
                
        return ans