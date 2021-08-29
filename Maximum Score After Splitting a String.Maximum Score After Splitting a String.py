# Sol 1

class Solution:

    def maxScore(self, s: str) -> int:
        i=0
        ans = 0
        for i in range(1,len(s)):
            left_sub = s[:i]
            right_sub = s[i:]
            ans = max(ans , left_sub.count("0")+ right_sub.count("1"))
        return ans
