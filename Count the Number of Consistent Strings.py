class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = []
        for word in words:
            count_bool = []
            for char in list(word):
                if char in list(allowed):
                    count_bool.append(True)
                else:
                    count_bool.append(False)
            result.append(all(count_bool))

        return sum(result) 
