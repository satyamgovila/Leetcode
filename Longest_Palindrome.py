class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        seen={}
        
        for i in s:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        count=0
        flag=0
        for i in seen:
            if seen[i]%2==0:
                count=count+seen[i]
                
            else:
                if seen[i]!=1:
                    count=count+seen[i]-1
                
                flag=1
                
           
        if flag==1:
            return count+1
        return count



########################################################################


	def longestPalindrome(self, s: str) -> int:
        d = collections.Counter(s)
        odd, ans = 0, 0
        
        for x in d:
            if d[x] % 2:
                odd += 1
            ans += d[x]

        return min(ans, ans - odd + 1)
