from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row=[0]*len(matrix);col=[0]*len(matrix[0])
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
                    
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0
                    
        
        return
                    
        
        