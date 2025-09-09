class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        result = []
        while(l<=r):
            left,right = abs(nums[l]),abs(nums[r])
            if(left>right):
                result.insert(0,left**2)
                l+=1
            else:
                result.insert(0,right**2)
                r-=1
        return result