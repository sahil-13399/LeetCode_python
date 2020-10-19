from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)==0:
            return 0
        val=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if val>prices[i]:
                val=prices[i]
            else:
                max_profit=max(max_profit,prices[i]-val)
        
        return max_profit
        