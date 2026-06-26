class Solution(object):
    def maxProfit(self, prices):
        minprice=float('inf')
        maxprice=0
        for price in prices:
            if price<minprice:
                minprice=price
            profit=price-minprice
            if profit>maxprice:
                maxprice=profit
        return maxprice

        