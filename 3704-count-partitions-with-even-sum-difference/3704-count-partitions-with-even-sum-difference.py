class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        length=len(nums)
        count=0
        for i in range(1,length):
            a1=nums[0:i]
            a2=nums[i:length]
            print(a1,a2)
            if (sum(a1)-sum(a2)) % 2 == 0:
                count+=1
        return count

        