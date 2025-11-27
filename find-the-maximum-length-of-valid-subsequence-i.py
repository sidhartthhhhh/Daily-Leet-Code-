class Solution(object):
    def maximumLength(self, nums):
        max_len = 0
        n = len(nums)

        count = 0
        for i in range(n):
            if nums[i] & 1 == 0:
                count += 1
        if count > max_len:
            max_len = count

        count = 0
        for i in range(n):
            if nums[i] & 1 == 1:
                count += 1
        if count > max_len:
            max_len = count

        count = 0
        expected = 0
        for i in range(n):
            if nums[i] & 1 == expected:
                count += 1
                expected = 1 - expected
        if count > max_len:
            max_len = count

        count = 0
        expected = 1
        for i in range(n):
            if nums[i] & 1 == expected:
                count += 1
                expected = 1 - expected
        if count > max_len:
            max_len = count

        return max_len