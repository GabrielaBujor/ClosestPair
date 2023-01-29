#Closest pair - divide-and-conquer algorithm

import math

#points = [(7, 3), (5, 4), (0, 0), (-2, 3), (-4, -2), (15, 7), (1, 5), (-4, 0)]

#points = [(1, 1), (0, 1), (1, 1), (1, 0)]

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

#points = [(7, 3), (5, 4), (0, 0), (2, 3), (4, 2), (15, 7), (1, 5), (3, 0)]

# points = [(70, 300), (50, 40), (0, 0), (-20, 30), (-400, -20), (150, 70), (10, 50), (-4, 0)]

# points = [(7.1, 3.2), (5.4, 4.2), (0, 0), (-2.2, 3.4), (-4.5, -2.4), (15.8, 7.7), (1.5, 5.3), (-4.7, 0)]


def closestPair(points):
    n = len(points)
    if n <= 3:
        return bruteForce(points)
    else:
        mid = n // 2
        leftSide = points[:mid]
        rightSide = points[mid:]
        (a1, b1) = closestPair(leftSide)
        (a2, b2) = closestPair(rightSide)
        (a3, b3) = closestSplitPair(points, a1, b1, a2, b2)
        d1 = dist(a1, b1)
        d2 = dist(a2, b2)
        d3 = dist(a3, b3)
        d = min(d1, d2, d3)
        if d == d1:
            return (a1, b1)
        elif d == d2:
            return (a2, b2)
        else:
            return (a3, b3)

def closestSplitPair(points, a1, b1, a2, b2):
    n = len(points)
    xMid = (points[n // 2][0] + points[n // 2 - 1][0]) / 2
    Arr = []
    for point in points:
        if abs(point[0] - xMid) < dist(a1, b1):
            Arr.append(point)
    bestPair = (a1, b1)
    bestDist = dist(a1, b1)
    Length = len(Arr)
    for i in range(Length):
        for j in range(i + 1, min(i + 7, Length)):
            if dist(Arr[i], Arr[j]) < bestDist:
                if Arr[i] != Arr[j]:
                    bestPair = (Arr[i], Arr[j])
                    bestDist = dist(Arr[i], Arr[j])
    return bestPair

def dist(a1, a2):
    return math.sqrt((a1[0] - a2[0])**2 + (a1[1] - a2[1])**2)

def bruteForce(points):
    n = len(points)
    bestPair = (points[0], points[1])
    bestDist = dist(points[0], points[1])
    for i in range(n):
        for j in range(i + 1, n):
            if dist(points[i], points[j]) < bestDist:
                if points[i] != points[j]:
                    bestPair = (points[i], points[j])
                    bestDist = dist(points[i], points[j])
    return bestPair

print(closestPair(points))
