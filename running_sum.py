"""
Running Sum of 1d Array
Given an array nums, we define a running sum of the array as:   runningSum[i] = sum(nums[0]...nums[i])

Constraints:
	•	The number of elements in the list is between [1, 1000].
	•	The value of each element in the array is between [-10^6, 10^6].

Example:
Input: nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
"""

# Solution 1
def running_sum(numbers: list) -> list:
	if not numbers:
		raise ValueError("Number must be a list of integers, cannot be empty.")
	
	if not isinstance(numbers, list):
		raise TypeError("NOT A LIST: Input must be a list of integers.")
	
	if not all(isinstance(num, int) for num in numbers):
		raise TypeError("NOT INTEGERS: Input must be a list of integers.")
	
	modified_nums = numbers.copy()
	for i in range(1, len(modified_nums)):
		modified_nums[i] += modified_nums[i-1]
	
	return modified_nums


# Solution 2
"""
from itertools import accumulate

def running_sum(numbers: list) -> list:
	if not numbers:
		raise ValueError("Number must be a list of integers, cannot be empty.")
	
	if not isinstance(numbers, list):
		raise TypeError("NOT A LIST: Input must be a list of integers.")
	
	if not all(isinstance(num, int) for num in numbers):
		raise TypeError("NOT INTEGERS: Input must be a list of integers.")

	return list(accumulate(numbers))
"""

# Solution 3
"""
def running_sum(nums: list) -> list:
	current_sum = 0
	return [current_sum := current_sum + num for num in nums]
"""