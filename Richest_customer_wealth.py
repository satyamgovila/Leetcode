class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for account in accounts:
            sum_acc = 0
            for j in account:
                sum_acc+=j
            res.append(sum_acc)
        return max(res)
        
