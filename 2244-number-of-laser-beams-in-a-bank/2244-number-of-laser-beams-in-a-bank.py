class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total=0
        m=len(bank[0])
        n=len(bank)
        arr=[]
        for floor in range(0,n):
            if int(bank[floor])==0:
                continue
            else:
                curr=0
                for i in range(0,m):
                    if bank[floor][i]=="1":
                        curr+=1
                arr.append(curr)
        res=0
        for i in range(1,len(arr)):
            res+=(arr[i]*arr[i-1])
        return res

        