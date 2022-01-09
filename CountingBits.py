'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''


# class Solution(object):
#     def countBits(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """

def countBits(n):
	ans = [0]
	for i in range(1, n+1):
		ans.append(len(bin(i)[2:].replace('0', '')))
	return ans

def dp_countBits(n):
	ans = [0]
	offset = 1
	for i in range(1, n+1):
		if (offset * 2) == i:
			offset = offset * 2
		ans.append(ans[i - offset] + 1)
	return ans

def best_countBits(n):
	ans = [0]
	offset = 1
	for i in range(1, n+1):
		ans.append(ans[i >> 1] + (i & 1))
	return ans


if __name__ == '__main__':
	countBits(20)
	dp_countBits(20)
	best_countBits(20)
