class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		cur = self
		output = [cur.val]
		while cur.next:
			cur = cur.next
			output += [cur.val]
		return ' -> '.join(map(str, output))

def ListNodeBuilder(xli):
	head = cur = ListNode(xli[0])
	for item in xli[1:]:
		new = ListNode(item)
		cur.next = new
		cur = new
	return head
################################################################################
class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not(head and head.next):
			return True

		left = []
		right = []

		slow = fast = head

		while fast and fast.next:
			left.append(slow.val)
			slow = slow.next
			fast = fast.next.next

		while slow:
			right.append(slow.val)
			slow = slow.next

		if len(right) > len(left):
			right = right[1:]

		return left == right[::-1]
################################################################################
class Solution(object):
	def isPalindrome(self, head):
		slow = fast = head
		rev = None

		while fast:
			if not fast.next:
				slow = slow.next
				break
			fast = fast.next.next
			rev, rev.next, slow = slow, rev, slow.next

		while rev and (slow.val == rev.val):
			rev = rev.next
			slow = slow.next

		print(slow, rev, sep='\n')
		return not rev

head = ListNodeBuilder([1, 2, 3, 2, 1])
obj = Solution()
obj.isPalindrome(head)
