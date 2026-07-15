# Last updated: 7/14/2026, 10:44:15 PM
1# class Solution:
2#     def maxProfit(self, prices: List[int]) -> int:
3#         max_profit = 0
4#         min_price = float('inf')
5
6#         for i in range(len(prices)):
7#             if prices[i]< min_price:
8#                 min_price= prices[i]
9#             elif prices[i]-min_price > max_profit:
10#                 max_profit = prices[i]-min_price
11
12#         return max_profit
13
14
15class Solution:
16    def maxProfit(self, prices: List[int]) -> int:
17        min_price = prices[0]
18        max_profit = 0
19        for price in prices:
20            if price<min_price:
21                min_price = price
22            
23            profit = price - min_price
24
25            if profit> max_profit:
26                max_profit = profit
27        return max_profit
28
29
30
31
32