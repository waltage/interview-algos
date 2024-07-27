class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def pprint(self, depth=1):
        print(self.value)
        if self.left:
            print(" " * depth, "L.", end="")
            self.left.pprint(depth + 1)
        if self.right:
            print(" " * depth, "R.", end="")
            self.right.pprint(depth + 1)


def tree_from_nodes(node_list: list[dict], root: str):
    node_vals = {}
    for n in node_list:
        node_vals[n["id"]] = BinaryTree(n["value"])

    for n in node_list:
        if n["left"] is not None:
            node_vals[n["id"]].left = node_vals[n["left"]]
        if n["right"] is not None:
            node_vals[n["id"]].right = node_vals[n["right"]]
    return node_vals[root]
