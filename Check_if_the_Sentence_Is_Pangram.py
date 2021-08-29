# Sol 1
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha_dict = {}
        for i in sentence:
            alpha_dict[i] = True
        return False if len(alpha_dict.keys()) < 26 else True
 

# Sol 2
 class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26
           
    
