# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion():
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n<2:
            return n
        s, e = 1, n
        while True:
            mid = (s+e)//2
            
            cr = isBadVersion(mid)
            pr = isBadVersion(mid-1)
            
            if cr and not pr:
                return mid
            elif cr:
                e = mid-1
            else:
                s = mid+1
            
        return -1