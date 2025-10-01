class Solution:
    def findLatestTime(self, s: str) -> str:
        new_str=list(s)
        if new_str[0]=='?':
            if new_str[1]=='?' or int(new_str[1])<=1:
                new_str[0]='1'
            else:
                new_str[0]='0'

        if new_str[1]=='?':
            if new_str[0]=='1':
                new_str[1]='1'
            else:
                new_str[1]='9'

        if new_str[3]=='?':
            new_str[3]='5'
        
        if new_str[4]=='?':
            new_str[4]='9'
        
        return ''.join(new_str)
        