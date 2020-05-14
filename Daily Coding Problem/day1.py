'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
n = 5
k =  17
numbers = [10, 4, 7]
def find_add(k):
	l = len(numbers)
	for i in range(l-1):
		base = numbers[i]
		for j in range(i+1, l):
			if numbers[i] +numbers[j] == k:
				return True
	

	return False

print(find_add(k))

''' Well that was easy '''

''' Langiappe: Do this for 3 numbers!'''

def find_add_3(k, l):
	for i in l:
		for j in l:
			for h in l:
				if i + j + h == k:
					return True
				elif i + j == k:
					return True
				elif j + h == k:
					return True
	return False

print(find_add_3(25, [10, 5, 10, 30, 45,11, 2]))

''' Second method '''