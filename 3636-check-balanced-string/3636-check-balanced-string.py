class Solution:
    def isBalanced(self, num: str) -> bool:
        odd,even=0,0
        flag=True
        for i in range(0,len(num)):
            if(flag==True):
                odd+=int(num[i])
            else:
                even+=int(num[i])
            flag=not flag
        return odd==even

        