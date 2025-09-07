class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        for i in range(1,n):
            out.append(i)
        m=n-1
        out.append(-(m*(m+1)//2))
        return out
        