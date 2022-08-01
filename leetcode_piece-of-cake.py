"""
DFS?

naive solution:
create a grid of the size of the cake (lol)

another way:
for each space between horizontal cuts, compute the area for each vertical cut
O(hw)

you can cache results with previous differences, but that doesn't help in the worst case
worst case is 1, 2, 3, etc. in differences between cuts

just literally find the biggest numbers of vert/horiz differences O(h+w)
"""


def maxArea(h, w, horizontalCuts, verticalCuts):
    horizontalCuts = sorted(horizontalCuts)
    verticalCuts = sorted(verticalCuts)
    maxHorizontal = 0
    maxVertical = 0
    prevCut = 0
    for cut in horizontalCuts:
        maxHorizontal = max(cut - prevCut, maxHorizontal)
        prevCut = cut
    maxHorizontal = max(h - prevCut, maxHorizontal)
    prevCut = 0
    for cut in verticalCuts:
        maxVertical = max(cut - prevCut, maxVertical)
        prevCut = cut
    maxVertical = max(w - prevCut, maxVertical)
    return (maxHorizontal * maxVertical) % ((10 ** 9) + 7)

h = 3
w = 5
horizontalCuts = [1]
verticalCuts = [1, 4]

print(maxArea(h, w, horizontalCuts, verticalCuts))
