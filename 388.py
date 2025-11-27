class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_lengths = {0: 0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
      
      
            if '.' in name:
                current_len = path_lengths[depth] + len(name)
                max_len = max(max_len, current_len)
            else:
                current_len = path_lengths[depth] + len(name) + 1
                path_lengths[depth + 1] = current_len
        
        return max_len