class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_result = [False]*len(candies)
        for candy in range(len(candies)):
            total_current = 0
            if (candies[candy]+ extraCandies) >= max(candies):
                bool_result[candy] = True
        return bool_result
