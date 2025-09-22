class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] +=1
            else:
                hash[i] = 1
        max_frq=max(hash.values())
        ret=0
        for i in hash.values():
            if i==max_frq:
                ret+=i
        return ret

            
        