class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i)-1
            nums[index] = -abs(nums[index])
        
        res = []
        for j,num in enumerate(nums):
            if num>0:
                res.append(j+1)

        return res