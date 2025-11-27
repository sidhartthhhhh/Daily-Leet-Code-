class Solution:
  def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    MOD = 10**9 + 7
    
    dp = [0] * (target + 1)
    dp[0] = 1  # There is 1 way to get a sum of 0 (with 0 dice)
    for _ in range(1, n + 1):
      new_dp = [0] * (target + 1)
     
      for j in range(1, target + 1):
        for f in range(1, k + 1):
        
          if j - f >= 0:
            new_dp[j] = (new_dp[j] + dp[j - f]) % MOD
            
    
      dp = new_dp
      
    return dp[target]