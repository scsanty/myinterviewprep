'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

def findDisappearedNumbers(nums: List[int]) -> List[int]:
	return list(set(range(1, len(nums)+1)) - set(nums))

# def best_findDisappearedNumbers(nums: List[int]) -> List[int]:
#     return


if __name__ == '__main__':
	print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
	print(findDisappearedNumbers([5, 2, 4, 1]))


