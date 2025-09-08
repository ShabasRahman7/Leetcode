class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=n//2
        b=n-a
        while('0' in str(a) or '0' in str(b)):
            a=a-7
            b=b+7
        return [a,b]