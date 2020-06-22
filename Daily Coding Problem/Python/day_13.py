'''
Given an integer k and a string s, find the longest substring that contains
at most k distinct characters

Example if k=2 and s = 'abcba'
the program would return 'bcb'

'''

k = 3
s = "abcdcba"
print(s)

#This one gonna be ugly and dumb

def count_unique(s):
	uniques = len(set(s))
	return uniques

def find_substring(k, s):
	substrings = []
	s = list(s)

	for x in reversed(range(len(s)+1)):
		for n in range(len(s)):
			current_string = s[n:x]
			if count_unique(current_string) == k:
				substrings.append(current_string)
			if len(current_string) == k:
				break

	current, previous = "", ""
	for x in substrings:
		current = x
		#print(previous, current)
		if len(current) > len(previous):
			previous = current




	return previous



print(find_substring(k, s))

k = 3
s = "onomonompea"

print(find_substring(k, s))