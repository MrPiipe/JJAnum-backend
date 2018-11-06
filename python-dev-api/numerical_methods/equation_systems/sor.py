import numpy as np
from numpy.lib.scimath import sqrt as csqrt


def sor(A, b, x0, tolerance, iterations, w):
    D = np.diag(np.diag(A))
    U = -1 * (np.triu(A) - D)
    L = -1 * (np.tril(A) - D)
    T, C = findProduct(D, U, L, b, w)

    count = 0
    dispersion = tolerance + 1
    print(spectralRadio(T))
    if spectralRadio(T) >= 1:
        raise Exception("Incorrect Spectral Radio")

    while dispersion > tolerance and count < iterations:
        x1 = np.matmul(T, x0) + C
        dispersion = np.linalg.norm(x1 - x0, 2)
        print(count, x1, dispersion)
        x0 = x1.copy()
        count = count + 1
    if dispersion < tolerance:
        print(x1, "is an initial approximation with a tolerance of {}".format(tolerance))
    else:
        print("Method failed in {} iterations".format(iterations))


def findProduct(D, U, L, b, w):
    D_wL_inv = np.linalg.inv(D - w*L)
    T = np.matmul(D_wL_inv, (1-w)*D + w*U)
    C = np.matmul(w * D_wL_inv, b)

    return T, C


def spectralRadio(A):
    v_prop, w = np.linalg.eig(A)
    return max(v_prop.min(), v_prop.max(), key=abs)


def main():
    matrix = [
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
    ]
    vector = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tolerance = 1e-7
    iterations = 100
    w = 1.4000
    sor(matrix, vector, x0, tolerance, iterations, w)


if __name__ == '__main__':
    main()
