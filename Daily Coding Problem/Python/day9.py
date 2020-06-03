'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

'''

example_1 = [2, 4, 6, 2, 5]
example_2 = [5, 1, 1, 5]
# I GitHubbed this one
def largest_sum(l):
    largest, prev = 0, 0
    for val in l:
        print(f"Value: {val}, Largest: {largest}, Previous: {prev}")
        prev, largest = largest, max(largest, prev + val)
        print(f"New Previous: {prev}, New Largest: {largest}")


largest_sum(example_1)