class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bal = prices[0]
        profit = 0
        for p in prices:
            if p < bal:
                bal = p
            else:
                potential = p - bal
                if potential > profit:
                    profit = potential
        return profit
                