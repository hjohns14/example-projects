
'''cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
 For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.'''

def cons(a, b):

	def pair(f):
		return f(a, b)
	return pair

def car(f):
	# Longer Way
	def fix(x, y):
		return x
	return f(fix)

def cdr(f):
	# Simpler way
	z = lambda x, y: y
	return f(z)



print(type(car))

l = cons(3, 5)
print(car(l))
