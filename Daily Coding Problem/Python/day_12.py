'''
There is a staircase with N number of steps and you can climp up 1 or 2
steps at a time. Given N, write a function that returns the number of unique
ways you can climb the staircase. The order of the steps matter.

For example if N = 5 then there are 8 unique ways
1,1,1,1,1
2,1,1,1
1,2,1,1
1,1,2,1
1,1,1,2
2,2,1
2,1,2
1,2,2
'''


def count_uniques(n):
	if n <= 1:
		return 1
	return count_uniques(n-1) + count_uniques(n-2)

assert count_uniques(4) == 5
assert count_uniques(2) == 2
assert count_uniques(5) == 8

print(count_uniques(10))

def fibbonaci(n):
	a, b = 1, 2
	for _ in range(n-1):
		a, b = b, a+b
	return a

assert fibbonaci(5) == 8
assert fibbonaci(4) == 5