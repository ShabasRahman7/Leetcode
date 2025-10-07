class Solution:
    def minimumPushes(self, word: str) -> int:
        length=len(word)
        m=length//8
        print(m)
        i=1
        count=0
        while(length>0):
            if(length-8>0):
                count+=i*8
                length-=8
            else:
                count+=i*length
                length=0
            i+=1
        return count

        