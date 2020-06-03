"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        if self.left and self.right:
            return_str = f"[l={self.left}  n={self.data}  r={self.right}]"
        elif self.left and not self.right:
            return_str =  f"[l={self.left}  n={self.data}]"
        elif self.right and not self.left:
            return_str = f"[n={self.data}  r={self.right}]"
        else:
            return_str = f"{self.data}"

        return return_str

    def insert(self, val=0, left=True):
        if left:
            self.left = Node(val)
        if not left:
            self.right= Node(val)


def count_unival(root):
    #Function that iterates over a tree and counts the number of unival subtrees
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left and root.data == root.right.data:
        return 1 + count_unival(root.right)
    elif not root.right and root.data == root.left.data:
        return 1 + count_unival(root.left)

    branch_count = count_unival(root.left) + count_unival(root.right)
    if root.right.data == root.data and root.left.data == root.data:
        parent_count = 1
    else:
        parent_count = 0
    return branch_count + parent_count  


# Creating the tree in the example
tree = Node(1)
tree.insert(1, True)
tree.insert(0, False)
tree.right.insert(1, True)
tree.right.insert(0, False)
tree.right.left.insert(1, True)
tree.right.left.insert(1, False)
print(tree)

assert count_unival(tree) == 5
assert count_unival(tree.left) == 1
assert count_unival(tree.right) == 4