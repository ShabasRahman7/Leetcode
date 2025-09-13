class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq_vowels={}
        freq_others={}
        vowels = ('a','e','i','o','u')
        for i in s:
            if i in vowels:
                if i in freq_vowels:
                    freq_vowels[i]+=1
                else:
                    freq_vowels[i]=1
            else:
                if i in freq_others:
                    freq_others[i]+=1
                else:
                    freq_others[i]=1
        max_vowels = max(freq_vowels.values()) if freq_vowels else 0
        max_others = max(freq_others.values()) if freq_others else 0
        return max_vowels+max_others        