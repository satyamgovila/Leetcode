class Solution(object):
    def wordPattern(self, pattern, str):
        slist = str.split()

        if len(pattern) != len(slist):
            return False
        return (len(set(pattern)) == len(set(slist)) == len(set(zip(pattern, slist))))
