class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d1 = collections.Counter(arr)
        return len(set(d1.values()) )==len(d1.values())
        
