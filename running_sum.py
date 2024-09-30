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
"""
def running_sum(nums: list) -> list:
	if not nums:
		return []
	
	for i in nums:
		nums[i] += nums[i-1] if i > 0 else nums[i]
"""

# Solution 2
"""
from itertools import accumulate

def running_sum(nums: list) -> list:
	return list(accumulate(nums))
"""

# Solution 3
def running_sum(nums: list) -> list:
	current_sum = 0
	return [current_sum := current_sum + num for num in nums]
