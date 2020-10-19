from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=0,0
        l=[]
        
        while(i<m and j<n):
            
            if(nums1[i]<=nums2[j]):
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
                
        while(i<m):
            l.append(nums1[i])
            i+=1
        while(j<n):
            l.append(nums2[j])
            j+=1
            
       # nums1=l.copy()
        for i in range(0,len(l)):
            nums1[i]=l[i]