class Solution:
    def totalMoney(self, n: int) -> int:
        arr=[1]
        for i in range(1,n):
            if(i%7==0):
                curr=arr[-7]+1
            else:
                curr=arr[-1]+1
            arr.append(curr)
        return sum(arr)
        


        