# Example 1:

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.


# Using Sort:

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    	s, t = sorted(s), sorted(t)
    	for i,j in enumerate(s):
    		if j != t[i]: return t[i]
    	return t[-1]


# Using Count:

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    	for i in set(t):
    		if s.count(i) != t.count(i): return i


# Using Counter:

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:        
        return list(collections.Counter(t) - collections.Counter(s))[0]
        
		
