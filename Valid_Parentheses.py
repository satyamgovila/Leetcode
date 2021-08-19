class Solution:
    def isValid(self, s: str) -> bool:   
        """
        :type s: str
        :rtype: bool
        """
        stack = ['N']
        m = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in m.keys():
                if stack.pop() != m[i]:
                    return False
            else:
                stack.append(i)
                
        return len(stack) == 1
