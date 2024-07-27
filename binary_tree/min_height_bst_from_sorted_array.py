"""
Given a sorted array of integers, construct a BST with minimal height.

TAGS:
- bst
- divide and conquer
- recursion
- master method: T(n) = 2 T(n/2) + Theta(1)

TIME COMPLEXITY:
- Theta(n) 
"""


def min_height_bst(array, left=0, right=None):
    # the array is sorted, meaning we can divide and conquer
    # fitting a root node in the middle of the array
    # and recursively fitting the left and right nodes

    if right is None:
        # initial case; set the right to the last index
        right = len(array) - 1
    if left > right:
        # protect off-by-one errors
        return None
    if left == right:
        # base case; return the node
        return BST(array[left])

    mid = (left + right) // 2

    node = BST(array[mid])
    node.left = min_height_bst(array, left, mid - 1)
    node.right = min_height_bst(array, mid + 1, right)

    return node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def pprint(self, depth=1):
        print(self.value)
        if self.left:
            print(" " * depth, "L.", end="")
            self.left.pprint(depth + 1)
        if self.right:
            print(" " * depth, "R.", end="")
            self.right.pprint(depth + 1)


if __name__ == "__main__":
    result = min_height_bst([1, 2, 5, 7, 10, 13, 14, 15, 22])

    result.pprint()
