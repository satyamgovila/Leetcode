# Example 1:

# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:

# Input: x = -101
# Output: false
    
class Solution:
    def isPalindrome(self, x):
        pal = x
        n = 0
        while x > 0:
            n = n * 10 + x % 10
            x = x //10
        if pal == n:
            return True
        else:
            return False
        
