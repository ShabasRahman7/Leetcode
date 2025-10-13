class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        length=len(words)-1
        i=1
        def get_freq(word):
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            return tuple(count)
            
        while(i<=length):
            if(len(words[i]) != len(words[i-1])):
                i+=1
            elif(get_freq(words[i]) == get_freq(words[i-1])):
                words.pop(i)
                length-=1
            else:
                i+=1
        return words

        