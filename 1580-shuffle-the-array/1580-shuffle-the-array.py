class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        l=len(x)
        res=[]
        for i in range(l):
            res.append(x[i])
            res.append(y[i])
        return res
