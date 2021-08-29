class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []

        for i in range(len(list(s))):
            if i%2 ==0:
                ans.append(s[i])
            else:
                ans.append(chr( ord(s[i-1]) + int(s[i])))

        return "".join(ans)
