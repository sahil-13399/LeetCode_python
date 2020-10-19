from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        
        for i in range(0,numRows):
            for j in range(0,i+1):
                x=[]
                if j==0:
                    x.append(1)
                    l.append(x)
                elif i==j:
                    l[i].append(1)
                else:
                    l[i].insert(j,l[i-1][j-1]+l[i-1][j])
            
        
        return l
                    
                
                
                
        