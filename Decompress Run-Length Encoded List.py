class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0 ,len(nums)-1 , 2):
            freq = nums[i]
            val = nums[i+1]
            res.extend([val]*freq)
        return res
        
