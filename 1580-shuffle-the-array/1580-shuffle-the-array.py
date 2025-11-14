class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        l=len(x)*2
        res=[0]*l
        n=0
        for i in range(l//2):
            res[n]=x[i]
            n+=1
            res[n]=y[i]
            n+=1
        return res
