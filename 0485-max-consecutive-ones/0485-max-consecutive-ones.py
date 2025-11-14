class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons=0
        maximum=0
        for i in nums:
            if i==1:
                cons+=1
                maximum=max(maximum,cons)
            else:
                cons=0
        return maximum
                

        