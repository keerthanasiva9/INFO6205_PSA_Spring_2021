#Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
# and node values with a subtree of s. A subtree of s is a tree consists of a node in s and
# all of this node's descendants. The tree s could also be considered as a subtree of itself.

#Example 1:
#Given tree s:
#     3
#    / \
#   4   5
#  / \
# 1   2

#Given tree t:
#   4
#  / \
# 1   2

#Return true, because t has the same structure and node values with a subtree of s.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return (root1.data == root2.data and
            check_identical(root1.left, root2.left) and
            check_identical(root1.right, root2.right)
            )

def isSubtree(T, S):
    if S is None:
        return True

    if T is None:
        return False

    if (check_identical(T, S)):
        return True

    return isSubtree(T.left, S) or isSubtree(T.right, S)


T = Node(3)
T.right = Node(5)
T.left = Node(4)
T.left.left = Node(1)
T.left.right = Node(2)

S = Node(4)
S.right = Node(2)
S.left = Node(1)

if isSubtree(T, S):
    print("True")
else:
    print("False")
