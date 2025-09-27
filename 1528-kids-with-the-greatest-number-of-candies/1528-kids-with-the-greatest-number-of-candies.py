class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        return [x+extraCandies >=maximum  for x in candies ]
        