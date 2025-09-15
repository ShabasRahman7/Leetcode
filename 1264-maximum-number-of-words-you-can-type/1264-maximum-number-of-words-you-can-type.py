class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = list(brokenLetters)
        string= text.split(' ')
        count=0
        for i in string:
            for j in broken:
                if j in i:
                    break
            else:
                count+=1
        return count

        