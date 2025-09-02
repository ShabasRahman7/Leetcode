class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start = 0
        row_end = len(matrix)-1
        col_start = 0
        col_end = len(matrix[0])-1

        res = []
        
        while(row_start<=row_end and col_start <= col_end):
            # left to right
            for i in range(col_start,col_end+1):
                res.append(matrix[row_start][i])
            
            row_start += 1

            # up to down
            for i in range(row_start,row_end+1):
                res.append(matrix[i][col_end])
            
            col_end -= 1

            # check for non square matrix
            if(row_start<=row_end and col_start<=col_end):
                # right to left
                for i in range(col_end,col_start-1,-1):
                    res.append(matrix[row_end][i])
            
                row_end -=1

                # bottom to up
                for i in range(row_end,row_start-1,-1):
                    res.append(matrix[i][col_start])

                col_start +=1

            
        
        return res