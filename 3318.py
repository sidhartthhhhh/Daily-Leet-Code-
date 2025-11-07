class Solution:
  def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    
    def _calculate_x_sum(subarray: List[int]) -> int:
      
      counts = Counter(subarray)
      
      distinct_elements = list(counts.items())
      
      if len(distinct_elements) < x:
        return sum(subarray)
        
      distinct_elements.sort(key=lambda item: (item[1], item[0]), reverse=True)
      

      top_x_pairs = distinct_elements[:x]
      
      x_sum = 0
      for value, freq in top_x_pairs:
        x_sum += value * freq
        
      return x_sum

    n = len(nums)
    answer = []
    
    for i in range(n - k + 1):

      subarray = nums[i : i + k]
      
      answer.append(_calculate_x_sum(subarray))
      
    return answer