# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    
    def __init__(self):
        
        self.cache = {}
    
    def climbStairs(self, n: int) -> int:    
        
        if n in self.cache:
            return self.cache[n]
        
        if n == 0 or n == 1:
            return 1
        
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.cache[n] = result
            return result
