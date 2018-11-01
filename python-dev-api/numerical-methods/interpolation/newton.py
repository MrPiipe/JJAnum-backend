import numpy as np
from math import exp, log


def function(matrix, arrayPoints):
    resultingFunction = "p(x) = "
    result = []
    for i in range(len(matrix)):
        if i != 0:
            x = np.round(arrayPoints[i-1, 0], 2)
            result.append("(x - {x})".format(x=x))

        const = np.round(matrix[i, i+1], 3)
        resultingFunction += str(const) + "".join(result) + " + "

    resultingFunction = resultingFunction[:-3]
    return resultingFunction


def newton(arrayPoints):
    n = len(arrayPoints)
    arrayPoints = np.matrix(arrayPoints)
    matrix = np.zeros((n, n+1))
    for i in range(n):
        matrix[i, 0] = arrayPoints[i, 0]
        matrix[i, 1] = arrayPoints[i, 1]

    k = 1
    for i in range(2, n+1):
        for j in range(i, n+1):
            fxk1 = matrix[j-1-1, i-1]
            fxk = matrix[j-1, i-1]
            xk1 = matrix[j-1, 0]
            xk = matrix[j-1-k, 0]
            matrix[j-1, i] = (fxk - fxk1) / (xk1 - xk)
        k += 1

    return function(matrix, arrayPoints)


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
    print(newton(arrayPoints))


if __name__ == '__main__':
    main()
