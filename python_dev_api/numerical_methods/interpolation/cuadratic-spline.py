import numpy as np
from sympy import sympify, expand


def equation(matrixPoints, arrayPoints):
    resultingFunction = []
    matrixPoints = np.round(matrixPoints, 2)
    n = len(arrayPoints) - 1

    for i in range(0, n*3, 3):
        function = "{a}*x**2 + {b}*x + {c}".format(
            a=matrixPoints[i],
            b=matrixPoints[i+1],
            c=matrixPoints[i+2],
        )

        function = str(sympify(function).expand())
        resultingFunction.append([function, "{x0} <= x <= {x1}".format(
            x0=arrayPoints[i//3, 0],
            x1=arrayPoints[i//3+1, 0]
        )])

    return resultingFunction


def cuadraticSpline(arrayPoints):
    n = len(arrayPoints) - 1
    arrayPoints = np.array(arrayPoints)
    matrix = np.zeros((n*3, n*3))
    vector = np.zeros(n*3)

    j = 0
    k = 0
    for i in range(0, n*2, 2):
        matrix[i, j+0] = arrayPoints[k, 0] ** 2
        matrix[i, j+1] = arrayPoints[k, 0]
        matrix[i, j+2] = 1
        matrix[i+1, j+0] = arrayPoints[k+1, 0] ** 2
        matrix[i+1, j+1] = arrayPoints[k+1, 0]
        matrix[i+1, j+2] = 1
        j += 3
        k += 1

    j = 1
    k = 0
    for i in range(n*2, n*3-1):
        matrix[i][k + 0] = 2 * arrayPoints[j, 0]
        matrix[i][k + 1] = 1
        matrix[i][k + 2+1] = - 2 * arrayPoints[j, 0]
        matrix[i][k + 3+1] = - 1
        j += 1
        k += 3

    matrix[n*3-1, 0] = 1
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
    print(np.round(result, 2))
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
    print(cuadraticSpline(arrayPoints))


if __name__ == '__main__':
    main()
