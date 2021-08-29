class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_dict= {"a" :1 , "e" :1 , "i" :1, "o" :1, "u" :1, "A" :1, "E" :1, "I" :1, "O" :1,            "U" :1}
        s = s.lower()

        l_count = r_count = 0

        for i in s[:int(len(s)/2)]:
            if i in vowel_dict:
                l_count+=1
        for i in s[int(len(s)/2):]:
            if i in vowel_dict:
                r_count+=1

        return l_count == r_count
