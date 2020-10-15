from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals)==0 or len(intervals)==1:
            return intervals
        
        intervals=sorted(intervals,key=lambda x:x[0])
        
        s=intervals[0][0];e=intervals[0][1]
        result=[]
        for i in range(1,len(intervals)):
            
            if(e>=intervals[i][0] and e<=intervals[i][1]):
                s=min(intervals[i][0],s)
                e=max(intervals[i][1],e)
            elif(e<intervals[i][0]):
                result.append([s,e])
                s=intervals[i][0];e=intervals[i][1]
        
        result.append([s,e])
        
        return result
        