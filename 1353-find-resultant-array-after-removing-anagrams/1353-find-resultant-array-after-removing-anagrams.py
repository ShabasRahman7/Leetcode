class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        length=len(words)-1
        i=1
        while(i<=length):
            if(len(words[i]) != len(words[i-1])):
                i+=1
            elif(Counter(words[i])==Counter(words[i-1])):
                words.pop(i)
                length-=1
            else:
                i+=1
        return words

        