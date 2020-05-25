### LINKED LISTS GOOD 2 KNOW
'''  first node         second             third 
         |                 |                 | 
         |                 |                 | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+ 

Linked list is made up of nodes.
Nodes contain data, and a pointer to the location of the next Node.
Python does not use pointers so this should be interesting


         first node             second                   third 
            |                      |                       | 
            |                      |                       | 
    +----+----+------+     +----+----+------+     +---+----+------+ 
    |null| 1  |   <--------->   | 2  |     <------->  |  3 | null | 
    +----+----+------+     +----+----+------+     +---+----+------+ 

XOR Linked list is made up of nodes.
It is the same as before but it can be traversed forward and in reverse


'''

# HERE is a simple linked list in python

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

		## I think this is harder to do XOR LL because python is dumb about stuff like this
		## we have no access to pointers(research pointers in python maybe?)


class LinkedList():
	def __init__(self):
		self.head = None

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

def create_links(llist, nodes):
	for i in range(len(nodes)):
		print(i)
		if nodes[i] == 0:
			llist.head = nodes[i]
		else:
			nodes[i]

nodes = [Node(1), Node(2), Node(3), Node(4)]
link_list = LinkedList()

link_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
link_list.head.next = second_node
second_node.next = third_node


create_links(link_list, nodes)


## ASOF 7-10-19: Giving up on this one because python is screwey. COME BACK
## Will be easier in C++