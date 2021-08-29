# Sol1

class Solution:
    def sortSentence(self, s: str) -> str:
        result = ""
        result_list = [""]* len(s)

        for word in s.split():
            word_loc = word[-1]
            print(word_loc)
            result_list[int(word_loc)] = word[0:-1]

        result = (" ".join(result_list)).rstrip().lstrip()
        return result
        
        
        
# Sol2


word_dict = {}
result = ""
result_list = [""]* len(s)



for word in s.split():
    word_loc = word[-1]
    print(word_loc)
    result_list[int(word_loc)] = word[0:-1]
    
    
print(" ".join(result_list))
