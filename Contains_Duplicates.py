class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
            d = collections.Counter(nums)
            for val in d.values():
                if val>=2:
                    return True
            return False
