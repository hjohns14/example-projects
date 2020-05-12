""" ISSUES:
1. All negative list should return a positive 1, but this does not happen. Currently returning 0
2. Clean up

"""

import numpy as np

ints = [-1, -2]

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

	return nums[-1] + 1

	print(nums)

print(lowest_pos_int(ints))