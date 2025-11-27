class Solution:
  def zigZagArrays(self, n: int, l: int, r: int) -> int:
    MOD = 10**9 + 7
    m = r - l + 1
    size = 2 * m
    
    # --- Helper: Matrix Multiplication ---
    def mat_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
      C = [[0] * size for _ in range(size)]
      for i in range(size):
        for j in range(size):
          # We can optimize this by checking if A[i][k] is 0
          for k in range(size):
            if A[i][k] != 0: # Small optimization
              C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
      return C
      
    # --- Helper: Matrix Power (Binary Exponentiation) ---
    def mat_pow(A: List[List[int]], k: int) -> List[List[int]]:
      res = [[0] * size for _ in range(size)]
      for i in range(size):
        res[i][i] = 1  # Identity matrix
        
      base = A
      while k > 0:
        if k % 2 == 1:
          res = mat_mul(res, base)
        base = mat_mul(base, base)
        k //= 2
      return res

    # --- Helper: Matrix-Vector Multiplication ---
    def mat_vec_mul(M: List[List[int]], V: List[int]) -> List[int]:
      res = [0] * size
      for i in range(size):
        for j in range(size):
          if M[i][j] != 0: # Small optimization
            res[i] = (res[i] + M[i][j] * V[j]) % MOD
      return res

    # 1. Build Transition Matrix T
    T = [[0] * size for _ in range(size)]
    for j in range(m):  # new value index (value l+j)
      for k in range(m):  # old value index (value l+k)
        if k < j:
          # from down[l+k] (index k+m) to up[l+j] (index j)
          T[j][k + m] = 1
        if k > j:
          # from up[l+k] (index k) to down[l+j] (index j+m)
          T[j + m][k] = 1
            
    # 2. Build Base Vector V_2 (for length 2)
    V_2 = [0] * size
    for j in range(m):
      val = l + j
      # up[val] = count [x, val] with l <= x < val
      V_2[j] = val - l
      # down[val] = count [x, val] with val < x <= r
      V_2[j + m] = r - val
        
    # 3. Calculate T^(n-2)
    exponent = n - 2
    T_final = mat_pow(T, exponent)
    
    # 4. Calculate V_n = T^(n-2) * V_2
    V_n = mat_vec_mul(T_final, V_2)
    
    # 5. Sum all entries in V_n
    ans = sum(V_n) % MOD
    return ans
        