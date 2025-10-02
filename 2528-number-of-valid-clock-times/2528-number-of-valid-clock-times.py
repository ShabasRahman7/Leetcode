class Solution:
    def countTime(self, time: str) -> int:
        h_option=0
        m_option=0

        h1,h2 = time[0],time[1]
        for h in range(24):
            hh=f"{h:02d}"
            if (h1=='?' or h1 == hh[0]) and (h2 =='?' or h2==hh[1]):
                h_option+=1
        
        m1,m2 = time[3],time[4]
        for m in range(60):
            mm=f"{m:02d}"
            if (m1=='?' or m1 == mm[0]) and (m2 =='?' or m2==mm[1]):
                m_option+=1

        return h_option*m_option