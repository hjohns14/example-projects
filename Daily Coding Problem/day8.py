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
        self.ut = 0

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


    def count_unival(self):
        #Function that iterates over a tree and counts the number of unival subtrees

        # ASOF 5-25-20 Im close but not done
        if not self.left and not self.right:
            self.ut += 1        
        elif self.data == self.left.data == self.right.data:
            self.ut += 1
            self.left.count_unival()
            self.right.count_unival()

        else:
            try:
                self.left.count_unival()
                self.right.count_unival()
            except AttributeError as e:
                pass
        print(self.ut)




    


# Creating the tree in the example
tree = Node(1)
tree.insert(1, True)
tree.insert(0, False)
tree.right.insert(1, True)
tree.right.insert(0, False)
tree.right.left.insert(1, True)
tree.right.left.insert(1, False)
print(tree)

tree.count_unival()