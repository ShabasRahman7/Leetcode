class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res=float('inf')
        start=0
        end=k-1
        while(end<=len(blocks)-1):
            times=0
            for i in range(start,end+1):
                if(blocks[i]=='W'):
                    times+=1
            print(times)
            res=min(res,times)
            start+=1
            end+=1
        return res
        