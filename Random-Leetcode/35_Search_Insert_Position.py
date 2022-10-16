class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        while (r-l)>1:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid
          
        if nums[l]>=target:
            return l
        return l+1