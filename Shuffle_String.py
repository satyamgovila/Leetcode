class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [x for x in sorted(zip(indices,[char for char in s]))]
        ans = ""
        for res in result:
            ans+= res[1]
        return ans
        
