class Solution:
  def lastRemaining(self, n: int) -> int:
    head = 1
    step = 1
    remaining_count = n
    is_left_to_right = True
    
    while remaining_count > 1:
    
      if is_left_to_right or (remaining_count % 2 == 1):
        head = head + step
        
      remaining_count = remaining_count // 2
      step = step * 2
      is_left_to_right = not is_left_to_right
    return head