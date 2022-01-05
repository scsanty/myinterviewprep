'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
'''


# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """


def climbStairs(n, memo={}):
	if n in memo:
		return memo[n]

	if n < 1:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		result = climbStairs(n-1, memo) + climbStairs(n-2, memo)
		memo[n] = result
		return result

def loop_climbStairs(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	y = 1
	x = 2
	for _ in range(n-2):
		temp = x
		x = x + y
		y = temp
	return x

def best_climbStairs(n):
	paths = [0] * (n+1)
	paths[0] = 1
	paths[1] = 1

	for i in range(2, n+1):
		paths[i] = paths[i-1] + paths[i-2]

	return paths[n]

if __name__ == '__main__':
	climbStairs(100)
