class Solution:
    def removeZeros(self, n: int) -> int:
        s = str(n)
        s_without_zeros = s.replace('0', '')
        return int(s_without_zeros)

