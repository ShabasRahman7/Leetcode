class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        wl = len(p)
        p_count = Counter(p)
        res = []
        for i in range(0,len(s)):
            string=s[i:i+wl]
            if p_count == Counter(string):
                res.append(i)
        return res