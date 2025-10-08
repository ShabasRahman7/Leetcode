class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        n=Counter(nums)
        ret=0
        for num,count in n.items():
            if count==1:
                ret+=num
        return ret
        