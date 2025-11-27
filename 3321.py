class Solution:
  def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    n = len(nums)
    answers = []
    
    # States for the sliding window
    freq = Counter()
    top_x = SortedList()
    others = SortedList()
    current_x_sum = 0
    current_total_sum = 0

    def get_pair(val):
      if val not in freq or freq[val] == 0:
        return None
      return (-freq[val], -val)

    def rebalance():
      nonlocal current_x_sum

      while len(top_x) < x and others:
        best_other_pair = others.pop(0)
        top_x.add(best_other_pair)
        # Adding to x-sum
        val = -best_other_pair[1]
        f = -best_other_pair[0]
        current_x_sum += val * f
        
      while top_x and others and top_x[-1] > others[0]:
        worst_top = top_x.pop(-1)
        best_other = others.pop(0)
        
        current_x_sum -= (-worst_top[1]) * (-worst_top[0])
        current_x_sum += (-best_other[1]) * (-best_other[0])
        
        top_x.add(best_other)
        others.add(worst_top)

    def add_val(val):
      nonlocal current_x_sum, current_total_sum
      current_total_sum += val
      old_freq = freq.get(val, 0)
      
      if old_freq > 0:
        old_pair = (-old_freq, -val)
        if old_pair in top_x:
          top_x.remove(old_pair)
          current_x_sum -= val * old_freq
        elif old_pair in others:
          others.remove(old_pair)
          
      # Adding new pair
      freq[val] += 1
      new_pair = get_pair(val)
      others.add(new_pair)
      
    def remove_val(val):
      nonlocal current_x_sum, current_total_sum
      current_total_sum -= val
      old_freq = freq[val]
      old_pair = get_pair(val)

      # Removing the old pair
      if old_pair in top_x:
        top_x.remove(old_pair)
        current_x_sum -= val * old_freq
      elif old_pair in others:
        others.remove(old_pair)
    
      freq[val] -= 1
      if freq[val] == 0:
        del freq[val]
      else:
        new_pair = get_pair(val)
        others.add(new_pair)

    for i in range(k):
      current_total_sum += nums[i]
      freq[nums[i]] += 1
      
    for val in freq:
      others.add(get_pair(val))
      
    rebalance()
    
    if len(freq) < x:
      answers.append(current_total_sum)
    else:
      answers.append(current_x_sum)

    for i in range(k, n):
      add_val(nums[i])
      remove_val(nums[i-k])
      rebalance()
      
      if len(freq) < x:
        answers.append(current_total_sum)
      else:
        answers.append(current_x_sum)
        
    return answers