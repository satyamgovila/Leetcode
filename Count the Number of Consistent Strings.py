# Sol 1
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        import collections
        allowed_dict = collections.Counter(allowed)
        result = []
        for word in words:
            count_bool = []
            for char in list(word):
                if char not in allowed_dict:
                    count_bool.append(False)
                    break
                else:
                    count_bool.append(True)
            result.append(all(count_bool))
        return sum(result) 
    
    
    # Sol 2
    
    class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        
        return len(words) - count
    
    
    
    
