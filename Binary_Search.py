class Solution:
    def binary_search(self , nums , left , right ,  target):
        if left > right:
            return -1
        mid = (left+right) // 2
        
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.binary_search(nums, left, mid-1, target)
        else:
            return self.binary_search(nums, mid+1, right, target)
               
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums , 0 , len(nums)-1 , target)
