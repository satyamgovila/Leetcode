class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        A = words
        for ch in set(A[0]):
            count = []
            for word in A:
                count.append(word.count(ch))
            res += ch * min(count)
        return res
