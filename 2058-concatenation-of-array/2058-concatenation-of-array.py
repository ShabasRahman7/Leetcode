class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [0]*(n*2)
        for i in range(0,n):
            ans[i],ans[n+i]=nums[i],nums[i]
        return ans