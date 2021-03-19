#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]

#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def reverse_node(self, l1, a):
        curr = l1

        for _ in range(a):
            if not curr:
                return l1
            curr = curr.next

        prev = None
        curr = l1

        for _ in range(a):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1.next = self.reverse_node(curr,a)

        return prev

    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

head1 = Node(1)
l1 = Node(2)
l2 = Node(3)
l3 = Node(4)
l4 = Node(5)

head1.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

a = 3

LL3 = Solution()
LL3.head = LL3.reverse_node(head1, a)
LL3.printLL()






