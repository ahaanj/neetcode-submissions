class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] # take the first element as the temporary min until we find a lower amount through iteration 
        max_profit = 0 #If we make it index 0 then we are assuming profit possible without even iterating through 

        for price in prices:
            min_price = min(min_price, price) #check if the next price is lower than the current, then update min price
            profit = price - min_price # if the min price is updated or still the same we not check what the availble proft is
            max_profit = max(max_profit,profit) # compare that calculated "max profit" price to the next profit difference and take the max 
        return max_profit

        