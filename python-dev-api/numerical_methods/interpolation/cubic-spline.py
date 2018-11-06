import numpy as np
from sympy import sympify


def equation(matrixPoints, arrayPoints):
    resultingEquation = []
    matrixPoints = np.round(matrixPoints, 2)
    n = len(arrayPoints) - 1

    j = 0
    for i in range(0, n*4, 4):
        function = "{a}*x**3 + {b}*x**2 + {c}*x + {d}".format(
            a=matrixPoints[i],
            b=matrixPoints[i+1],
            c=matrixPoints[i+2],
            d=matrixPoints[i+3],
        )
        function = str(sympify(function).expand())
        resultingEquation.append([function, "{x0} <= x <= {x1}".format(
            x0=arrayPoints[j, 0],
            x1=arrayPoints[j+1, 0]
        )])
        j += 1

    return resultingEquation


def cubicSpline(arrayPoints):
    n = len(arrayPoints) - 1
    arrayPoints = np.array(arrayPoints)
    matrix = np.zeros((n*4, n*4))
    vector = np.zeros(n*4)

    j = 0
    k = 0
    for i in range(0, n*2-1, 2):
        matrix[i, j+0] = arrayPoints[k, 0] ** 3
        matrix[i, j+1] = arrayPoints[k, 0] ** 2
        matrix[i, j+2] = arrayPoints[k, 0]
        matrix[i, j+3] = 1
        matrix[i+1, j+0] = arrayPoints[k+1, 0] ** 3
        matrix[i+1, j+1] = arrayPoints[k+1, 0] ** 2
        matrix[i+1, j+2] = arrayPoints[k+1, 0]
        matrix[i+1, j+3] = 1
        j += 4
        k += 1

    j = 1
    k = 0
    for i in range(n*2, n*3-1):
        matrix[i][k + 0] = 3 * arrayPoints[j, 0]**2
        matrix[i][k + 1] = 2 * arrayPoints[j, 0]
        matrix[i][k + 2] = 1
        matrix[i][k + 3+1] = - 3 * arrayPoints[j, 0]**2
        matrix[i][k + 4+1] = - 2 * arrayPoints[j, 0]
        matrix[i][k + 5+1] = - 1
        j += 1
        k += 4

    j = 1
    k = 0
    for i in range(n*3-1, n*4-2):
        matrix[i][k + 0] = 6 * arrayPoints[j, 0]
        matrix[i][k + 1] = 2
        matrix[i][k + 3+1] = - 6 * arrayPoints[j, 0]
        matrix[i][k + 4+1] = - 2
        j += 1
        k += 4

    matrix[n*4-2, 0] = 6 * arrayPoints[0, 0]
    matrix[n*4-2, 1] = 2
    matrix[n*4-1, n*4-4] = 6 * arrayPoints[n, 0]
    matrix[n*4-1, n*4-3] = 2

    vector[0] = arrayPoints[0, 1]
    j = 1
    for i in range(1, n):
        vector[j] = arrayPoints[i, 1]
        vector[j+1] = arrayPoints[i, 1]
        j += 2
    vector[n*2-1] = arrayPoints[n, 1]
    result = np.linalg.solve(matrix, vector)

    # print(matrix)
    # print(vector)
    print(result)
    return equation(result, arrayPoints)


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

    print(cubicSpline(arrayPoints))


if __name__ == '__main__':
    main()
