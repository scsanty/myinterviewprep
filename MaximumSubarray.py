'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """


def maxSubArray(nums): # O(n^2)
	"""
	:type nums: List[int]
	:rtype: int
	"""
	maxsum = nums[0]
	len_n = len(nums)
	startidx = endidx = 0
	for i in range(len_n):
		for j in range(i, len_n):
			cursum = sum(nums[i:j+1])
			if maxsum < cursum:
				maxsum = cursum
				startidx = i
				endidx = j+1

	return nums[startidx : endidx]

def best_maxSubArray(nums): # O(n) Kadane's Algo
	"""
	:type nums: List[int]
	:rtype: int
	"""
	maxsum = nums[0]
	cursum = nums[0]
	len_n = len(nums)
	startidx = curstartidx = endidx = 0
	for i, n in enumerate(nums[1:], start=1):
		cursum += n
		if cursum < n:
			cursum = n
			curstartidx = i
		if maxsum < cursum:
			maxsum = cursum
			startidx = curstartidx
			endidx = i

	return nums[startidx : endidx]

if __name__ == '__main__':
	print('[5,4,-1,7,8]:', maxSubArray([5,4,-1,7,8]))
	print('[-2,1,-3,4,-1,2,1,-5,4]:', maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

	import random
	xt = [random.randint(-10**4, 10**4) for _ in range(10**5)]

	import time
	start = time.time()
	res = best_maxSubArray(xt)
	end = time.time()
	print(res, end-start)
