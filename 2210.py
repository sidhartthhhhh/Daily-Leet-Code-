class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Step 1: Remove consecutive duplicates
        compact = [nums[0]]
        for num in nums[1:]:
            if num != compact[-1]:
                compact.append(num)

        count = 0
        # Step 2: Check for hills and valleys
        for i in range(1, len(compact) - 1):
            if compact[i] > compact[i - 1] and compact[i] > compact[i + 1]:
                count += 1  # Hill
            elif compact[i] < compact[i - 1] and compact[i] < compact[i + 1]:
                count += 1  # Valley

        return count