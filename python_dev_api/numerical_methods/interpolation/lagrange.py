from sympy import sympify, simplify


def lagrange(x, y):
    n = len(x)
    result = []
    equation = ""

    for i in range(0, n):
        numerator = ""
        denominator = ""
        for j in range(0, n):
            if j is not i:
                numerator += "(x" + "-" + str(x[j]) + ")*"
                denominator += ("("+str(x[i]) + "-" + str(x[j]) + ")*")
        numerator = numerator[:-1]
        denominator = denominator[:-1]
        resultAux = str(y[i]) + "*" + numerator + "/" + denominator
        result.append(resultAux)

    for i in result:
        equation += "(" + i + ")" + "+"
    equation = equation[:-1]

    equation = sympify(equation)
    equation = simplify(equation)
    return("p(x) = " + str((equation)))


def main():
    x = [1.0000, 2.0000, 3.0000, 4.0000, 5.0000,
        6.0000, 7.0000, 8.0000, 9.0000, 10.0000]
    y = [0.5949, 0.2622, 0.6028, 0.7112, 0.2217,
        0.1174, 0.2967, 0.3188, 0.4242, 0.5079]
    print(lagrange(x, y))


if __name__ == '__main__':
    main()
