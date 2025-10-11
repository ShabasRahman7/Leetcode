class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashTable={}
        for i,num in enumerate(nums):
            if num in hashTable and i-hashTable[num]<=k:
                return True
            hashTable[num]=i
        return False
        