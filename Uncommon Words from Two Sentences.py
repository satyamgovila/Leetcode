class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        import collections
        d1 = collections.Counter(s1.split())
        d2 = collections.Counter(s2.split())

        result = []


        for k,v in (d1+d2).items():
            if v==1:
                result.append(k)
        return result
