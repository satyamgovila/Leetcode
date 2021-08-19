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
        
