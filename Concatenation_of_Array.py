class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = [None]*2*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]

        for i in range(len(nums)):
            ans[len(nums)+i] = nums[i]
        return ans
