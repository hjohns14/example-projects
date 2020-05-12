'''Given an array of integers, return a new array such that each element at index i of 
the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6]. '''


import numpy as np

arg = [3, 2, 1]

def  factorial(arg):
	final = []
	for j in range(len(arg)):
		new_arg = list(arg)
		new_arg.remove(arg[j])
		result = 1
		for i in new_arg:
			result  = result * i
		final.append(result)
		#print(final)
	return final
