class Solution:
    def hasSameDigits(self, s: str) -> bool:
        res=s
        while(len(res)>2):
            length=len(res)
            new_str=""
            for i in range(1,length):
                new_str += str((int(res[i-1]) + int(res[i]))%10)
            res=new_str
        return res[0]==res[1]
