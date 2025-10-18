class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        distinct_count=0
        prev_max=float('-inf')
        nums.sort()
        for num in nums:
            lower_bound=num-k
            upper_bound=num+k

            if prev_max<lower_bound:
                prev_max=lower_bound
                distinct_count+=1
            elif(prev_max<upper_bound):
                prev_max+=1
                distinct_count+=1
        return distinct_count
                
        