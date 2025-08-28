class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x1,x2 = points.pop()
        res = 0
        while points:
            y1,y2 = points.pop()
            res += max(abs(y1-x1),abs(y2-x2))
            x1,x2 = y1,y2
        return res