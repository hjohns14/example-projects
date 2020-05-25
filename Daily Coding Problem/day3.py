'''   This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
For example, given the following Node class
	class Node:
	    def __init__(self, val, left=None, right=None):
	        self.val = val
	        self.left = left
	        self.right = right
The following test should pass:
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

index = 0

class Node():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def serialize(root, output):
		if not root:
			output.append('#')
			return
		output.append(root.val)
		Node.serialize(root.left, output)
		Node.serialize(root.right, output)
		

	def deserialize(source):
		global index
		if source[index] == '#':
			index += 1
			return None
		value = source[index]
		index += 1
		left = Node.deserialize(source)
		right = Node.deserialize(source)
		return Node(value, left, right)






root = 	Node('root', 
	   		Node('left', 
	   			Node('left.left'),
	   			Node('left.right')),
	   		Node('right',
	   			Node('right.left'),
	   			Node('right.right')))
result = []
Node.serialize(root, result)
print(result)
new_root = Node.deserialize(result)
final_answer = []
Node.serialize(new_root, final_answer)
print(result)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert node.deserialize(serialize(node)).left.left.val == 'left.left'

## LOTS OF RECURSION ## LEARN IT, LOVE IT ###

# This was my first attempt and failure

'''def serialize(root):
	## TURN THE TREE INTO A STRING ##
	root_string = []

	root_val = root.val
	root_string.append(root_val)
	parent = root.left

	while parent is not None:
		first_val = parent.val
		left_child = parent.left
		right_child = parent.right
		if type(parent.left) == str:
			root_string.append(left_child)

		if type(parent.right) == str:
			root_string.append(right_child)

		elif type(left_child) != str:
			parent = left_child
		elif type(right_child) != str:
			parent = right_child

		root_string.append(first_val)

	parent = root.right
	while parent is not None:
		first_val = parent.val
		left_child = parent.left
		right_child = parent.right
		if type(parent.left) == str:
			root_string.append(left_child)

		if type(parent.right) == str:
			root_string.append(right_child)

		elif type(left_child) != str:
			parent = left_child
		elif type(right_child) != str:
			parent = right_child

		root_string.append(first_val)

	return root_string


'''