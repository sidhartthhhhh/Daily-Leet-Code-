class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    
    chars_counts = collections.Counter(chars)
    
    total_good_length = 0
    for word in words:
      
      word_counts = collections.Counter(word)
      is_good = True
      for char, count_needed in word_counts.items():
    
        if chars_counts[char] < count_needed:
          is_good = False
          break
          
      if is_good:
        total_good_length += len(word)
        
    return total_good_length
        