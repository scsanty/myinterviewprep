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
        count =0

        while fast and fast.next:
            left.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            count += 1

        print(count)

        while slow:
            right.append(slow.val)
            slow = slow.next

        if len(right) > len(left):
            right = right[1:]

        return left == right[::-1]

def ListNodeBuilder(xli):
    head = cur = ListNode(xli[0])
    for item in xli[1:]:
        new = ListNode(item)
        cur.next = new
        cur = new
    return head

head = ListNodeBuilder([1, 2, 3, 2, 1])
obj = Solution()
obj.isPalindrome(head)
