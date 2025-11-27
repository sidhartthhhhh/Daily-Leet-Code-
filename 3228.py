class Solution:
    def maxOperations(self, s: str) -> int:
        # ones_bef = 0
        # ans = 0
        # i = 0
        # n = len(s)

        # while i < n:
        #     if s[i] == '1':
        #         ones_bef += 1
        #         i += 1
        #     else:
        #         j = i
        #         while j < n and s[j] == '0':
        #             j += 1
        #         zeros = j - i
        #         ans += min(ones_bef, zeros)
        #         i = j
        # return ans

        ones = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1

            elif i >0 and s[i-1] == '1':
                ans += ones
                # if ones > 0:
                #     ops += 1
                #     ones -= 1
                # ops += zeros
        return ans