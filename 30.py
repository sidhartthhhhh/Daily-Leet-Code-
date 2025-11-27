class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)

        if total_len >  n:
            return []

        word_count = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0

            for right in range (offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    seen[word] += 1
                    count +=1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == num_words:
                        result.append(left)
                        
                        # moving left one word forward for the next window
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # reseting the window if the word is invalid
                    seen.clear()
                    count = 0
                    left = right + word_len
        
        return result