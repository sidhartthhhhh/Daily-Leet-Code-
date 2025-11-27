1. Two Sum (Array, Hash Map)
   - Scan once, store visited value → index in a map, checking whether `target - num` already exists. Complexity O(n) time, O(n) space.
2. Add Two Numbers (Linked List, Simulation)
   - Walk both lists digit by digit with carry propagation, appending to a dummy head list. Complexity O(max(m, n)).
3. Longest Substring Without Repeating Characters (Sliding Window)
   - Move right pointer adding chars to map; shrink left when duplicate found to keep window unique. Complexity O(n).
4. Median of Two Sorted Arrays (Binary Search)
   - Perform binary search on smaller array to partition both halves so left max ≤ right min, then compute median. Complexity O(log(min(m, n))).
5. Longest Palindromic Substring (Expand Around Center)
   - Expand from each index (odd and even centers), tracking longest span. Complexity O(n²) time, O(1) space.
6. Zigzag Conversion (String Manipulation)
   - Simulate row traversal by toggling direction while filling strings for each row, then concatenate. Complexity O(n).
7. Reverse Integer (Math)
   - Pop digits via mod/divide, push into result while checking 32-bit overflow before multiplication/addition. Complexity O(log₁₀ n).
8. String to Integer (atoi) (Parsing)
   - Trim spaces, parse optional sign, accumulate digits while clamping to 32-bit range. Complexity O(n).
9. Palindrome Number (Math)
   - Reject negatives, reverse half the digits and compare to remaining half to avoid overflow. Complexity O(log₁₀ n).
10. Regular Expression Matching (Dynamic Programming)
    - DP on pattern/text positions; handle `*` by zero or more of preceding char, `.` as wildcard. `dp[i][j]` indicates match. Complexity O(mn).
11. Container With Most Water (Two Pointers)
    - Two pointers from ends; move the shorter line inward updating max area. Complexity O(n).
12. Integer to Roman (Math)
    - Greedy subtract with ordered value-symbol pairs (including subtractive forms). Complexity O(1) with fixed set.
13. Roman to Integer (Math)
    - Iterate characters, subtract value when smaller than next, otherwise add. Complexity O(n).
14. Longest Common Prefix (String)
    - Compare characters across all strings or sort and compare first/last. Complexity O(n·k).
15. 3Sum (Two Pointers)
    - Sort array, fix one index, use two-pointer sweep skipping duplicates to find zero sum triplets. Complexity O(n²).
16. 3Sum Closest (Two Pointers)
    - Sort, then fixed pointer + two-pointer, tracking minimal absolute difference. Complexity O(n²).
17. Letter Combinations of a Phone Number (Backtracking)
    - Map digits to letters, perform DFS building string path per digit. Complexity O(4ⁿ).
18. 4Sum (Two Pointers)
    - Sort, use two nested loops and two-pointer inner search, skipping duplicates. Complexity O(n³).
19. Remove Nth Node From End of List (Linked List)
    - Two pointers separated by n nodes; when fast hits end, slow.next is target. Requires dummy head. Complexity O(L).
20. Valid Parentheses (Stack)
    - Push opening brackets; on closing ensure stack top matches pair. Valid if stack empty. Complexity O(n).
21. Merge Two Sorted Lists (Linked List)
    - Merge like merge-sort using dummy head, always append smaller node. Complexity O(m+n).
22. Generate Parentheses (Backtracking)
    - DFS track counts of open/close; add '(' if open < n, ')' if close < open. Complexity Catalan number.
23. Merge k Sorted Lists (Heap)
    - Initialize min-heap with head of each list, repeatedly extract min and push next node. Complexity O(N log k).
24. Swap Nodes in Pairs (Linked List)
    - Iterate with dummy prev pointer swapping two nodes at a time by re-pointing. Complexity O(n).
25. Reverse Nodes in k-Group (Linked List)
    - For each k-block, reverse by pointer manipulation; leave remainder as is. Complexity O(n).
26. Remove Duplicates from Sorted Array (Two Pointers)
    - Maintain slow pointer for write position, skip duplicates by comparing with last unique. Complexity O(n).
27. Remove Element (Two Pointers)
    - Iterate, copying elements ≠ val to front; return new length. Complexity O(n).
28. Implement strStr() (String)
    - Use KMP (build prefix table) or sliding window; first match index returned or -1. Complexity O(n+m).
29. Divide Two Integers (Math)
    - Handle signs, use bit shifts to subtract largest multiples of divisor; clamp to 32-bit limits. Complexity O(log n).
30. Substring with Concatenation of All Words (Sliding Window)
    - Use word frequency map; slide window in word-size strides, adjusting counts and start pointer to maintain valid multiset. Complexity O(n·word_len).
31. Next Permutation (Math)
    - Find first decreasing index from right, swap with next larger element, reverse tail. Complexity O(n).
32. Longest Valid Parentheses (Stack/Dynamic Programming)
    - Stack indices (seeded with -1); push on '(' and use length difference on ')' when stack non-empty; reset base otherwise. Complexity O(n).
33. Search in Rotated Sorted Array (Binary Search)
    - Modified binary search determining which side is sorted and searching accordingly. Complexity O(log n).
34. Find First and Last Position of Element in Sorted Array (Binary Search)
    - Two binary searches for lower/upper bounds. Complexity O(log n).
35. Search Insert Position (Binary Search)
    - Standard binary search returning left pointer insertion spot. Complexity O(log n).
36. Valid Sudoku (Matrix)
    - Track sets for each row, column, sub-box; ensure new digits unseen. Complexity O(1) since grid fixed 9×9.
37. Sudoku Solver (Backtracking)
    - Recursive DFS selecting empty cell, trying digits that satisfy row/col/box constraints, backtracking if invalid. Complexity exponential in blanks.
38. Count and Say (String)
    - Iteratively build next term by counting consecutive digits in current string. Complexity O(n·length(term)).
39. Combination Sum (Backtracking)
    - Sort array, DFS adding candidates (allow reuse) while tracking remaining target; prune when exceed. Complexity exponential.
40. Combination Sum II (Backtracking)
    - Similar to Combination Sum but skip duplicates by iterating with index and not reusing same element. Complexity exponential.
41. First Missing Positive (Array)
    - Use index mapping: iterate, place each value v in position v-1 via swaps; scan for first mismatch. Complexity O(n) time, O(1) extra space.
42. Trapping Rain Water (Two Pointers)
    - Two pointers with left/right max tracking; add trapped water from shorter side each step. Complexity O(n).
43. Multiply Strings (Math)
    - Simulate multiplication using int array of size m+n storing partial sums, handle carries, trim leading zeros. Complexity O(mn).
44. Wildcard Matching (Dynamic Programming)
    - DP where `*` matches any sequence, `?` matches single char; optimize to 1D or use greedy two-pointer with backtracking. Complexity O(mn).
45. Jump Game II (Greedy)
    - Track current farthest reachable and next farthest; increment jumps when moving to next layer. Complexity O(n).
46. Permutations (Backtracking)
    - DFS swapping or using used-array to explore all orderings. Complexity O(n·n!).
47. Permutations II (Backtracking)
    - Sort numbers, skip duplicates by checking previous identical unused element. Complexity O(n·unique permutations).
48. Rotate Image (Matrix)
    - Transpose square matrix then reverse each row (or layer-by-layer 4-way swap). Complexity O(n²).
49. Group Anagrams (Hash Map)
    - Sort each string (or count letters) to canonical key, append to map; return grouped lists. Complexity O(n·k log k).
50. Pow(x, n) (Binary Exponentiation)
    - Fast exponentiation by repeated squaring; handle negative exponent by inverting base. Complexity O(log n).

