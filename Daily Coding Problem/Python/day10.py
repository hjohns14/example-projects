"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Apple.
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import time
def f():
	print("Hey")


def scheduler(f, n):
	start = time.time()
	while True:
		if time.time() - start > n/1000:
			f()
			break


scheduler(f, 2000)