class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        item_dict = { "type" : 0 , "color" : 1 , "name" :2}

        for item in items:
            if item[item_dict[ruleKey]] == ruleValue:
                count+=1
        return count
        
