class Solution(object):
    def rotate(self, matrix):
        x=len(matrix)
        for i in range(x):
            for j in range(i+1,x):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(x):
            matrix[i].reverse()


        