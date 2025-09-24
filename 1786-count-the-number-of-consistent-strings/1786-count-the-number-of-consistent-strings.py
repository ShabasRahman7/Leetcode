class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allo=set(allowed)
        count=0
        for i in words:
            for j in i:
                if j not in allo:
                    break
            else:
                count+=1
        return count