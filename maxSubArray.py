class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        lsum=nums[0];gsum=nums[0]
        
        for i in range(1,len(nums)):
            
            lsum=max(nums[i],lsum+nums[i])
            gsum=max(lsum,gsum)
            
        return gsum
        