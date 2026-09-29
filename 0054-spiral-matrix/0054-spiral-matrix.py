class Solution(object):
    def spiralOrder(self, matrix):
        min_row=0
        min_col=0
        max_row=len(matrix)
        max_col=len(matrix[0])
        
        a=[]
        while min_row<max_row and min_col<max_col:
              
            for col in range(min_col,max_col):
                a.append(matrix[min_row][col])
            min_row+=1
            for row in range(min_row,max_row):
                a.append(matrix[row][max_col-1])
            max_col-=1
            if min_row<max_row and min_col<max_col:
                 
                for col in range(max_col-1,min_col-1,-1):
                    a.append(matrix[max_row-1][col])
                max_row-=1
                for row in range(max_row-1,min_row-1,-1):
                    a.append(matrix[row][min_col])
                min_col+=1
        return a

        

        