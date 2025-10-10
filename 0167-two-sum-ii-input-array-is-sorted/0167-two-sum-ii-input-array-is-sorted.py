class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash={
            numbers[0]:1
        }
        for i in range(1,len(numbers)):
            print(hash)
            a=target-numbers[i]
            if a in hash.keys():
                return [hash[a],i+1]
            else:
                hash[numbers[i]]=i+1