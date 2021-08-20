# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        for val in nums:
            if val in dic:
                dic[val]+=1
            else:
                dic[val]=1
        count= 0
        for val in dic.values():
            count+= (val*(val-1))/2
        return int(count)
