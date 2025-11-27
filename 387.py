class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
                
        return -1