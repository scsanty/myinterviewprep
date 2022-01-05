'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

def singleNumber(nums):    
    nums = sorted(nums)
    return (set(nums[::2]) - set(nums[1::2])).pop()

def best_singleNumber(nums):
	# XOR returns 1 only if in 1 otherwise returns 0 if both are 1

    #  101
    #  001
    # =101
    dup = 0
    for n in nums:
        dup ^= n
    return dup


if __name__ == '__main__':
	singleNumber([5, 2, 4, 1])


