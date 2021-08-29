# Sol 1

class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)

# Sol 2

class Solution:
    def toLowerCase(self, str): 
        return str.lower()
