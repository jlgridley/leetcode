import math


def countPoints(points, queries):
    answer = []
    for xq, yq, r in queries:
        pointCount = 0
        for xp, yp in points:
            if math.sqrt(math.pow(xp-xq, 2) + math.pow(yp-yq, 2)) <= r:
                pointCount += 1
        answer.append(pointCount)
    return answer



points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]

print(countPoints(points, queries))
