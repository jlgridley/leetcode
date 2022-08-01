def maxFrequency(nums, k):
    nums_sorted = sorted(nums)
    left = 0
    max_freq = 1
    curr_diff = 0
    for i in range(1, len(nums_sorted)):
        new_diff = nums_sorted[i] - nums_sorted[i-1]
        new_diff * (i - left)


    return max_freq

print(maxFrequency([3,9,6], 200))



"""
k = 10

1 2 3 4 7 . . .
3 7 9
      3

"""
