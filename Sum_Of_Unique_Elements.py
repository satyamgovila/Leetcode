class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d1 = collections.Counter(nums)
        arr = [k for k,v in d1.items() if v==1 ]
        return sum(arr)
