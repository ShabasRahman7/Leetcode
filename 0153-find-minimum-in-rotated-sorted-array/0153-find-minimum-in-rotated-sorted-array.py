class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        while(start<=end):
            if nums[start]<=nums[end]:
                return nums[start]
            mid=(start+end)//2
            if mid<end and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif mid>0 and nums[mid]< nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid-1