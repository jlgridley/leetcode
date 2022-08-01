"""
0 1 2
1 1 1
"""

def minOperations(nums):
    if len(nums) == 1:
        return 0
    operations = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            increase = nums[i-1] - nums[i] + 1
            operations += increase
            nums[i] += increase
    return operations





nums = [1,5,2,4,1]
print(minOperations(nums))
