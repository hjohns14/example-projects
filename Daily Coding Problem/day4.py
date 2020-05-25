"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place. 


ISSUES:
1. All negative list should return a positive 1, but this does not happen. Currently returning 0
2. Clean up

"""

import numpy as np

ints = [-1, -3, -5]

def lowest_pos_int(source):
	nums = sorted(set(source))
	j = 0
	for i in nums:
		if i < 0:
			nums.remove(i)

		
	while j < len(nums)-1:
		
		eq = nums[j+1]


		if eq - nums[j] != 1:
			error_occured = True
			print("ERROR at index ", j)
			fix = nums[j] + 1
			return fix
	

		j += 1

	if nums[-1] + 1 < 0:
		return 1
	else:
		return nums[-1] + 1

	print(nums)

print(lowest_pos_int(ints))