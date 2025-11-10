class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        candidates.sort()
        
        def backtrack(remaining_target: int, current_path: List[int], start_index: int):
        
            if remaining_target == 0:
                results.append(list(current_path))
                return
            if remaining_target < 0:
                return
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                current_path.append(candidate)
                backtrack(remaining_target - candidate, current_path, i)
                current_path.pop()
                
        backtrack(target, [], 0)
        return results