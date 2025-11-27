class Solution(object):
    def maximumLength(self, nums):
        parities = [num % 2 for num in nums]
        n = len(parities)
        max_len = 0

        # there are 4 possible patterns to try:
        patterns = [
            [0],       # all even
            [1],       # all odd
            [0, 1],    # even, odd, even, ...
            [1, 0]     # odd, even, odd, ...
        ]

        for pattern in patterns:
            ptr = 0  # pattern pointer
            length = 0
            for p in parities:
                if p == pattern[ptr]:
                    length += 1
                    ptr = (ptr + 1) % len(pattern)
            max_len = max(max_len, length)

        return max_len