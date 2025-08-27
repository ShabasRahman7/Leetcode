class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_list = sorted(nums)
        d = {}

        for i,val in enumerate(new_list):
            if val not in d:
                d[val] = i
            
        res = []
        for i in nums:
            res.append(d[i])

        return res