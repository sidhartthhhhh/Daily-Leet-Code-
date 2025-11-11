class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []
        for s in strs:
            z = s.count('0')
            o = len(s) - z
            if z <= m and o <= n:
                counts.append((z, o))

        dp = [[0]* (n+1) for _ in range(m + 1)]

        for z , o in counts:
            for i in range (m, z-1, -1):
                row = dp[i]
                prev_row = dp [i-z]
                for j in range (n, o-1, -1):
                    card = prev_row[j - o] + 1
                    if card > row[j]:
                        row[j] = card
        return dp[m][n]