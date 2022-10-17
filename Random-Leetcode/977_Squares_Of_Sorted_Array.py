#Two Pointer Solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, res = 0, len(nums)-1, [0]*len(nums)
        while l<=r:
            lv = nums[l]
            rv = nums[r]
            if abs(lv)>abs(rv):
                res[r-l] = (lv*lv)
                l+=1
            else:
                res[r-l] = (rv*rv)
                r-=1        
        return res