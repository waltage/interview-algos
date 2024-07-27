"""
Given two binary trees, return a new binary tree that represents
an overlay of the two trees. Each node in the new tree should
should have a value that is the sum of the values of the
same corresponding node in each of the trees.  If a node has no
corresponding node in the other tree, the returned node value
should be equal to the value of the node that is present.

TAGS:
- binary tree
- recursion
- master method: T(n) = 2 T(n/2) + Theta(1)

TIME COMPLEXITY:
- Theta(n)

"""

from typing import Optional

from helpers import BinaryTree, tree_from_nodes


def merge_trees(
    t1: Optional[BinaryTree] = None, t2: Optional[BinaryTree] = None
) -> BinaryTree:
    if not t2:
        return t1
    if not t1:
        return t2
    n = BinaryTree(t1.value + t2.value)
    n.left = merge_trees(t1.left, t2.left)
    n.right = merge_trees(t1.right, t2.right)
    return n


if __name__ == "__main__":

    result = merge_trees(
        tree_from_nodes(
            [
                {"id": "2", "left": "3", "right": "6", "value": 2},
                {"id": "3", "left": None, "right": "4", "value": 3},
                {"id": "6", "left": None, "right": "7", "value": 6},
                {"id": "4", "left": None, "right": None, "value": 4},
                {"id": "7", "left": None, "right": None, "value": 7},
            ],
            "2",
        ),
        tree_from_nodes(
            [{"id": "7", "left": None, "right": None, "value": 7}],
            "7",
        ),
    )
    result.pprint()
