class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_pixel=0
        line = 1
        for char in s:
            l_code = ord(char)-97
            curr_pixel = widths[l_code]
            if total_pixel+curr_pixel > 100:
                line+=1
                total_pixel=0
            total_pixel+=curr_pixel
        return [line,total_pixel]
        