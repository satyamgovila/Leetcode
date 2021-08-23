class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_till_now = 0
        result = []

        for i in range(0, len(nums)):
            sum_till_now += nums[i]
            result.append(sum_till_now)
        return result
