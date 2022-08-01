class Node:
    def __init__(self, value, index, num_nums):
        self.value = value
        self.index = index
        self.num_nums = num_nums

def get_sums(arr):
    sums = []
    root = Node(arr[0], 0, 1)
    stack = [root]
    while stack:
        curr = stack.pop()
        sums.append((curr.value, curr.num_nums))
        if curr.index < len(arr) - 1:
            next = curr.index + 1
            child1 = Node(curr.value + arr[next], next, curr.num_nums + 1)
            stack.append(child1)
            child2 = Node(arr[next] + curr.value - arr[curr.index], next, curr.num_nums)
            stack.append(child2)
    return sums

"""
          1
     /       \
   2 + 1      2
    /  \     /   \
  7+3   7+1 7+2   7

"""

def splitArraySameAverage(nums):
    l = len(nums)
    if l == 1:
        return False
    if l == 2:
        return nums[0] == nums[1]
    A = nums[:l//2]
    B = nums[l//2:]

    sumsA = get_sums(A)
    sumsB = get_sums(B)
    total = sum(nums)
    for Asum, Anum in sumsA:
        if Asum/Anum == (total - Asum) / (l - Anum):
            return True
    for Bsum, Bnum in sumsB:
        if Bsum/Bnum == (total - Bsum) / (l - Bnum):
            return True
    print(len(sumsA))
    print(len(sumsB))
    for Asum, Anum in sumsA:
        for Bsum, Bnum in sumsB:
            if (l == Anum + Bnum):
                continue
            curr_average = (Asum + Bsum) / (Anum + Bnum)
            if (curr_average == (total - Asum - Bsum) / (l - Anum - Bnum)):
                return True

    return False

nums = [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
print(splitArraySameAverage(nums))
