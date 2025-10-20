class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res =[-1]*2
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]>target):
                right=mid-1
            elif(nums[mid]<target):
                left=mid+1
            elif(nums[mid]==target):
                i,j=mid,mid
                while(i>0 and nums[i-1]==nums[i]):
                    print("i=",i)
                    i-=1

                while(j<len(nums)-1 and nums[j+1]==nums[j]):
                    print("j=",j)
                    j+=1
                res[0],res[1] = i,j
                break
        return res

        