class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash={}
        for i in range(0,len(numbers)):
            a=target-numbers[i]
            if a in hash.keys():
                return [hash[a],i+1]
            else:
                hash[numbers[i]]=i+1