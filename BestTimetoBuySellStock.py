'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """


def maxProfit(prices):
	maxprice = prices[-1]
	maxprofit = 0

	for p in prices[-2::-1]:
		maxprice = max(maxprice, p)
		profit = maxprice - p
		maxprofit = max(maxprofit, profit)
	return maxprofit

def best_maxProfit(prices):
	low = prices[0]
	high = 0
	best = 0
	for price in prices:
		if price < low:
			low = price
			high = 0
		if price > high:
			high = price
			if (high - low) > best:
				best = high - low

	if (best) < 0:
		return 0
	else:
		return best

if __name__ == '__main__':
	maxProfit([7,1,5,3,6,4])
