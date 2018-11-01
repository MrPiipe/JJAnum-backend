import numpy as np
from numpy.lib.scimath import sqrt as csqrt


def gaussEliminationTotalPivot(A, b):
    augmented, marks = elimination(A, b)

    A = np.delete(augmented.copy(), len(augmented), 1)
    b = augmented[:, len(augmented)]

    x = regressiveSustitution(A, b)
    x = organiceMarks(x,  marks)

    return x


def elimination(A, b):
    augmented = np.concatenate((A, b.T), axis=1)

    n = len(augmented)
    marks = np.arange(1, n+1)

    for k in range(0, n-1):
        augmented, marks = totalPivot(augmented, marks, n, k)
        for i in range(k+1, n):
            mult = augmented[i, k]/augmented[k, k]
            for j in range(k, n+1):
                augmented[i, j] = augmented[i, j] - mult * augmented[k, j]

    return augmented, marks


def totalPivot(augmented, marks, n, k):
    maxNum = 0
    maxRow = k
    maxCol = k
    for r in range(k, n):
        for s in range(k, n):
            if abs(augmented[r, s]) > maxNum:
                maxNum = abs(augmented[r, s])
                maxRow = r
                maxCol = s
    if maxNum == 0:
        raise Exception("System has no solution")
    else:
        if maxRow != k:
            augmented = exchangeRows(augmented, maxRow, k)
        if maxCol != k:
            augmented = exchangeCols(augmented, maxCol, k)
            marks = exchangeMarks(marks, maxCol, k)
        return augmented, marks


def exchangeRows(augmented, maxRow, k):
    augmented[[k, maxRow]] = augmented[[maxRow, k]]
    return augmented


def exchangeCols(augmented, col_mayor, k):
    augmented[:, [k, col_mayor]] = augmented[:, [col_mayor, k]].copy()
    return augmented


def exchangeMarks(marks, i, j):
    marks[i], marks[j] = marks[j], marks[i]
    return marks


def organiceMarks(x, marks):
    sortedX = np.zeros(len(marks))

    for i in range(len(marks)):
        pos = marks[i] - 1
        sortedX[pos] = x[int(i)]
    return sortedX


def regressiveSustitution(U, z):
    n = len(U)
    x = np.zeros(n)
    x[n-1] = z[n-1]/U[n-1, n-1]

    for i in range(n-2, -1, -1):
        total = 0
        for p in range(n-1, i, -1):
            total = total + U[i, p] * x[p]
        x[i] = (z[i]-total)/U[i, i]

    return x


def main():
    matrix = np.matrix([
        [9.1622, 0.4505, 0.1067, 0.4314, 0.8530,
            0.4173, 0.7803, 0.2348, 0.5470, 0.5470],
        [0.7943, 9.0838, 0.9619, 0.9106, 0.6221,
            0.0497, 0.3897, 0.3532, 0.2963, 0.7757],
        [0.3112, 0.2290, 9.0046, 0.1818, 0.3510,
            0.9027, 0.2417, 0.8212, 0.7447, 0.4868],
        [0.5285, 0.9133, 0.7749, 9.2638, 0.5132,
            0.9448, 0.4039, 0.0154, 0.1890, 0.4359],
        [0.1656, 0.1524, 0.8173, 0.1455, 9.4018,
            0.4909, 0.0965, 0.0430, 0.6868, 0.4468],
        [0.6020, 0.8258, 0.8687, 0.1361, 0.0760,
            9.4893, 0.1320, 0.1690, 0.1835, 0.3063],
        [0.2630, 0.5383, 0.0844, 0.8693, 0.2399,
            0.3377, 9.9421, 0.6491, 0.3685, 0.5085],
        [0.6541, 0.9961, 0.3998, 0.5797, 0.1233,
            0.9001, 0.9561, 9.7317, 0.6256, 0.5108],
        [0.6892, 0.0782, 0.2599, 0.5499, 0.1839,
            0.3692, 0.5752, 0.6477, 9.7802, 0.8176],
        [10.0000, 0.4427, 0.8001, 0.1450, 0.2400,
            0.1112, 0.0598, 0.4509, 0.0811, 20.0000]
    ])
    vector = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    x = gaussEliminationTotalPivot(matrix, vector)
    print(x)


if __name__ == '__main__':
    main()
