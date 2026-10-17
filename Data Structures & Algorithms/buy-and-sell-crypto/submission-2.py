class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given unsorted array prices where you're allowed to buy once and sell once
        # and we want to end with the highest profit

        # one solution would be a nested for loop that goes through all the combinations
        # to find the largest profit but that would be O(n^2) time complexity

        # to get to O(n) we could do a sliding window where the moment we hit a local
        # minimum value then that becomes the new potential buy and the moment we hit 
        # a profit then that's a sell candidate

        minimum = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                p = prices[i] - minimum

                if profit < p:
                    profit = p        
        return profit