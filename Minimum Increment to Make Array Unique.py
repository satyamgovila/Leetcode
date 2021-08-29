class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if nums == [] or len(nums)==1: # Base Cases
            return 0
        nums.sort()                    # We sort the array
        s, ans, mx = set(), 0, nums[0] # We initialize a set, the ans variable and max value as 'mx'
        for num in nums:
            if num in s:               # if num exists already
                mx = mx + 1            # we need to make it as current max + 1
                ans += (mx - num)      # we calculate steps required to do so. Eg: mx = 6, num = 3, so steps are 3
                s.add(mx)              # we add new max value in set, next number will be 1 more than this value
            else:
                s.add(num)
                mx = max(mx, num)
        return ans
