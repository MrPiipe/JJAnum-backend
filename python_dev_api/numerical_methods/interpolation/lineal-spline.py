import numpy as np
from sympy import sympify


def generateVector(startPoint, endPoint):
    vector = "{fx1} + ({fx1} - {fx0})/({x1} - {x0})*(x - {x1})".format(
        fx1=endPoint[1],
        fx0=startPoint[1],
        x1=endPoint[0],
        x0=startPoint[0])

    print(vector)
    return sympify(vector)


def linealSpline(arrayPoints):
    arrayPoints = np.array(arrayPoints)
    n = len(arrayPoints)
    splines = []
    for i in range(n-1):
        vector = generateVector(arrayPoints[i], arrayPoints[i+1])
        splines.append(vector)

    resultingFunction = []
    for i in range(n-1):
        resultingFunction.append([splines[i], "{x0} <= x <= {x1}".format(
            x0=arrayPoints[i][0], x1=arrayPoints[i+1][0])])

    return resultingFunction


def main():
    arrayPoints = [[1.0000, 0.5949],
                   [2.0000, 0.2622],
                   [3.0000, 0.6028],
                   [4.0000, 0.7112],
                   [5.0000, 0.2217],
                   [6.0000, 0.1174],
                   [7.0000, 0.2967],
                   [8.0000, 0.3188],
                   [9.0000, 0.4242],
                   [10.0000, 0.5079]]

    print(linealSpline(arrayPoints))


if __name__ == '__main__':
    main()
