class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j=set(jewels)
        count=0
        for c in stones:
            if c in j:
                count+=1
        return count