# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} # key  = nums[i] , value = index of nums[i]
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [ hash_table[nums[i]] , i ]
            else:
                hash_table[target - nums[i] ] = i
                
            
        
        
