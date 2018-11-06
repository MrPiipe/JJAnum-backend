import numpy as np


def function(resultingEquation):
    n = len(resultingEquation)
    resultingFunction = "p(x) = "
    for i in range(n-1):
        resultingFunction = resultingFunction + \
            str(resultingEquation[i]) + "x^" + str(n-i-1) + " + "

    resultingFunction = resultingFunction + str(resultingEquation[n-1])
    return resultingFunction


def equation(x, n):
    resultingEquation = []
    for i in range(n-1, -1, -1):
        resultingEquation.append(x**i)

    return np.array(resultingEquation)


def vandermonde(arrayPoints):
    arrayPoints = np.array(arrayPoints)
    n = len(arrayPoints)
    vandermondeMatrix = []

    for i in range(n):
        x = arrayPoints[i][0]
        y = arrayPoints[i][1]
        fila = equation(x, n)
        vandermondeMatrix.append(fila)

    vandermondeMatrix = np.array(vandermondeMatrix)
    vectorB = arrayPoints[:, 1].copy()

    print(vandermondeMatrix)
    # print(vectorB)
    vectorA = np.linalg.solve(vandermondeMatrix, vectorB)
    resultingFunction = function(np.round(vectorA, 4))
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

    print(vandermonde(arrayPoints))


if __name__ == '__main__':
    main()
