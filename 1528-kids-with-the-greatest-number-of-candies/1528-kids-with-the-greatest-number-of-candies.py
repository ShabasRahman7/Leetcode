class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        for i in range(0,len(candies)):
            if candies[i]+extraCandies>=maximum:
                candies[i]=True
            else:
                candies[i]=False
        return candies
        