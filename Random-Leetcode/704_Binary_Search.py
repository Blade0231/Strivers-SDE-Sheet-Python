class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        x = 0
        while n>0:
            if n%2==0:
                mid = int(n/2)
            else:
                mid = int((n-1)/2)
            
            if nums[mid] == target:
                return x+mid
            elif nums[mid] > target:
                nums = nums[:mid]
            else:
                nums = nums[mid+1:]
                x+=mid+1
                
            n = len(nums)
            
        return -1