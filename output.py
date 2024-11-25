import numpy as np
from tabulate import tabulate
from polynom import Polynomial


tabulate.WIDE_CHARS_MODE = True


class Output:

    @staticmethod
    def ShowLambda(LambdaMatrix, DimY):
        Header = ['Y1', 'Y2', 'Y3', 'Y4']
        Out = f"Матриця λ для Y:\n"
        Out += tabulate(LambdaMatrix.T, Header[:DimY], floatfmt=('.4f',)*LambdaMatrix.shape[0],
                        tablefmt="double_outline")
        Out += "\n\n"
        return Out

    @staticmethod
    def ShowPsi(psi, DimY):
        Out = ""
        for i in np.arange(DimY):
            Out += f"Матриця ψ для Y{i+1}:\n"
            SubPsi = np.vstack(psi[i])
            Out += tabulate(SubPsi.T, floatfmt=('.4f',)*SubPsi.shape[0], tablefmt="double_outline")
            Out += "\n"
        return Out

    @staticmethod
    def ShowA(A, DimY):
        Header = ['Y1', 'Y2', 'Y3', 'Y4']
        Out = f"Матриця a для Y:\n"
        Out += tabulate(A.T, Header[:DimY], floatfmt=('.4f',)*A.shape[0], tablefmt="double_outline")
        Out += "\n\n"
        return Out

    @staticmethod
    def ShowPhi(Phi, DimY):
        Out = ""
        for i in np.arange(DimY):
            Out += f"Матриця Ф для Y{i + 1}:\n"
            SubPhi = np.vstack(Phi[i])
            Out += tabulate(SubPhi.T, floatfmt=('.4f',)*Phi.shape[0], tablefmt="double_outline")
            Out += "\n"
        return Out

    @staticmethod
    def ShowC(c, DimY):
        Header = ['Y1', 'Y2', 'Y3', 'Y4']
        Out = f"Матриця c для Y:\n"
        Out += tabulate(c.T, Header[:DimY], floatfmt=('.4f',)*c.shape[0], tablefmt="double_outline")
        Out += "\n\n"
        return Out

    @staticmethod
    def ShowDependenceByPhi(c, DimY):
        """Вивід функціональної залежності через функції Ф."""
        Out = "\nФункціональна залежність від Ф:\n\n"
        for i in np.arange(DimY):
            Out += f"Ф{i+1}(X1,X2,X3) = {c[i][0]:.4f}Ф{i+1}1(X1) + {c[i][1]:.4f}Ф{i+1}2(X2) + {c[i][2]:.4f}Ф{i+1}3(X3)\n"
        return Out

    @staticmethod
    def GetCoefficient(a, c, LambdaMatrix, Dimm, Degrees, i, j, p):
        """Повертає коефіцієнт при T{p}(x{i}{j})."""
        Dim = Dimm[:i - 1]
        Deg = Degrees[:i - 1]  # + 1
        Coefficient = c[i - 1]
        Coefficient *= a[sum(Dim) + j - 1]
        Coefficient *= LambdaMatrix[np.sum(np.multiply(Dim, Deg)) + p]
        return Coefficient

    @classmethod
    def ShowDependenceByPolynomials(Cls, a, c, LambdaMatrix, Dim, Degrees, PolynomialType, DimY):
        """Вивід функціональної залежності через поліноми T."""

        def GetTerm(_i, _j, _p, __i):
            """Повертає коефіцієнт при T{p}(x{i}{j}) у готовій для запису формі."""
            Coefficient = Cls.GetCoefficient(a[__i], c[__i], LambdaMatrix[__i], Dim, Degrees, i, j, p)
            if _i == 1 and _j == 1 and _p == 0:
                Sign = ""
            elif Coefficient >= 0:
                Sign = " + "
            else:
                Sign = " - "
            Coefficient = abs(Coefficient)
            return f"{Sign}{Coefficient:.4f}*T{_p}(x{_i}{_j})"

        Out = "\nФункціональна залежність від поліномів:\n"
        for _i in np.arange(DimY):
            Out += f"\nФ{_i+1}(X1,X2,X3) = "
            for i in np.arange(1, 4):  # i = 1 ... 3
                for j in np.arange(1, Dim[i-1]+1):  # j = 1 ... dim[d]
                    for p in np.arange(Degrees[i-1]+1):  # p = 0 ... degrees[i]
                        Out += GetTerm(i, j, p, _i)
            Out += "\n"
        return Out

    @classmethod
    def ShowNormalizedDependenceByVariables(Cls, a, c, LambdaMatrix, Dim, Degrees, PolynomialType, DimY):
        """Вивід функціональної залежності через нормалізовані змінні X."""

        def GetTerm(i, j, p, PolynomialCoefficients):
            """Повертає коефіцієнт при x{_i}{_j}^{_p} у готовій для запису формі."""
            Coefficient = PolynomialCoefficients[p]
            if i == 1 and j == 1 and p == 1:
                Sign = ""
            elif Coefficient > 0:
                Sign = " + "
            elif Coefficient < 0:
                Sign = " - "
            else:
                return ""
            Coefficient = abs(Coefficient)
            return f"{Sign}{Coefficient:.4f}*x{i}{j}^{p}"

        polynomial = Polynomial(PolynomialType)
        Out = f"\nФункціональна залежність від змінних (з нормалізацією):\n\n"
        for i in np.arange(DimY):

            Out += f"Ф{i+1}(X1,X2,X3) = "
            PolynomialMultipliers = list()
            for i in np.arange(1, 4):  # i = 1 ... 3
                PolynomialMultipliers.append(list())
                for j in np.arange(1, Dim[i-1]+1):  # j = 1 ... dim[d]
                    PolynomialMultipliers[i-1].append(list())
                    for p in np.arange(Degrees[i-1]+2):  # p = 0 ... degrees[i]
                        coefficient = Cls.GetCoefficient(a[i], c[i], LambdaMatrix[i], Dim, Degrees, i, j, p)
                        PolynomialMultipliers[i-1][j-1].append(coefficient)

            FreeTerm = 0  # Вільний член, не прив'язаний до Х.
            for i in np.arange(1, 4):  # i = 1 ... 3
                for j in np.arange(1, Dim[i-1]+1):  # j = 1 ... dim[d]
                    PolynomialCoefficients = polynomial.GetPolynomialSumCoefficients(Degrees[i-1],
                                                                                          PolynomialMultipliers[i-1][j-1])
                    for p in np.arange(Degrees[i-1]+1):
                        if p == 0:
                            FreeTerm += PolynomialCoefficients[p]
                        else:
                            Out += GetTerm(i, j, p, PolynomialCoefficients)
            if FreeTerm > 0:
                Out += f"+{FreeTerm:.4f}"
            elif FreeTerm < 0:
                Out += f"{FreeTerm:.4f}"
            Out += "\n\n"
        return Out

    @classmethod
    def ShowDependenceByVariables(Cls, a, c, LambdaMatrix, Dim, Degrees, PolynomialType, YMin, YMax, DimY):
        """Вивід функціональної залежності через ненормалізовані(звичайні) змінні X."""

        def GetTerm(i, j, p, PolynomialCoefficients, YMin, YMax):
            """Повертає коефіцієнт при x{_i}{_j}^{_p} у готовій для запису формі."""
            Coefficient = PolynomialCoefficients[p] * (YMax-YMin)
            if i == 1 and j == 1 and p == 1:
                Sign = ""
            elif Coefficient > 0:
                Sign = " + "
            elif Coefficient < 0:
                Sign = " - "
            else:
                return ""
            Coefficient = abs(Coefficient)
            return f"{Sign}{Coefficient:.5f}*x{i}{j}^{p}"

        polynomial = Polynomial(PolynomialType)
        Out = f"Функціональна залежність від змінних (відновлена):\n\n"
        for I in np.arange(DimY):
            Out += f"Ф{I+1}(X1,X2,X3) = "

            PolynomialMultipliers = list()
            for i in np.arange(1, 4):  # i = 1 ... 3
                PolynomialMultipliers.append(list())
                for j in np.arange(1, Dim[i-1]+1):  # j = 1 ... dim[d]
                    PolynomialMultipliers[i-1].append(list())
                    for p in np.arange(Degrees[i-1]+2):  # p = 0 ... degrees[i]
                        coefficient = Cls.GetCoefficient(a[I], c[I], LambdaMatrix[I], Dim, Degrees, i, j, p)
                        PolynomialMultipliers[i-1][j-1].append(coefficient)

            FreeTerm = 0  # Вільний член, не прив'язаний до Х.
            for i in np.arange(1, 4):  # i = 1 ... 3
                for j in np.arange(1, Dim[i-1]+1):  # j = 1 ... dim[d]
                    PolynomialCoefficients = polynomial.GetPolynomialSumCoefficients(Degrees[i-1],
                                                                                          PolynomialMultipliers[i-1][j-1])
                    for p in np.arange(Degrees[i-1]+1):
                        if p == 0:
                            FreeTerm += PolynomialCoefficients[p]
                        else:
                            Out += GetTerm(i, j, p, PolynomialCoefficients, YMin[I], YMax[I])
            FreeTerm = YMin[I] + FreeTerm * (YMax[I]-YMin[I])
            if FreeTerm > 0:
                Out += f"+{FreeTerm:.4f}"
            elif FreeTerm < 0:
                Out += f"{FreeTerm:.4f}"
            Out += "\n\n"
        return Out

    @staticmethod
    def ShowError(Error, ErrorNormalized, DimY):
        Header = ['Y1', 'Y2', 'Y3', 'Y4']
        Out = "Нормалізовані помилки:\n"
        ErrorNormalized = np.reshape(ErrorNormalized, (-1, 1))
        Out += tabulate(ErrorNormalized.T, Header[:DimY], floatfmt=('.4f',)*DimY, tablefmt="double_outline")
        Out += '\n'
        Out += "Відновлені помилки:\n"
        Error = np.reshape(Error, (-1, 1))
        Out += tabulate(Error.T, Header[:DimY], floatfmt=('.4f',)*DimY, tablefmt="double_outline")
        Out += "\n"
        return Out

    @classmethod
    def ShowSpecial(Cls, Solver, DimY):
        """Отримує i-тий номер стовпця y та функцію виводу out. Виводить всі дані для y{i}."""
        LambdaMatrix = Solver.LmbdMatrix
        Psi = Solver.Psi
        A = Solver.a
        Phi = Solver.Phi
        C = Solver.c
        Error = Solver.Error
        Error_normalized = Solver.ErrorNormalized
        Dim = np.array((Solver.DimX1Value, Solver.DimX2Value, Solver.DimX3Value))
        Degrees = np.array((Solver.X1DegreeValue, Solver.X2DegreeValue, Solver.X3DegreeValue))
        PolynomialType = Solver.PolynomValue
        YMax = tuple(np.max(Solver.Y[i]) for i in np.arange(DimY))
        YMin = tuple(np.min(Solver.Y[i]) for i in np.arange(DimY))
        Out = Cls.ShowLambda(LambdaMatrix, DimY)
        Out += Cls.ShowPsi(Psi, DimY)
        Out += Cls.ShowA(A, DimY)
        Out += Cls.ShowPhi(Phi, DimY)
        Out += Cls.ShowC(C, DimY)
        Out += Cls.ShowDependenceByPhi(C, DimY)
        Out += Cls.ShowDependenceByPolynomials(A, C, LambdaMatrix, Dim, Degrees, PolynomialType, DimY)
        Out += Cls.ShowNormalizedDependenceByVariables(A, C, LambdaMatrix, Dim, Degrees, PolynomialType, DimY)
        Out += Cls.ShowDependenceByVariables(A, C, LambdaMatrix, Dim, Degrees,
                                                 PolynomialType, YMin, YMax, DimY)
        Out += Cls.ShowError(Error, Error_normalized, DimY)
        return Out

    @classmethod
    def show(Cls, Solver):
        """Виводить дані на TextBrowser та записує їх у текстовий файл."""
        Out = ""
        for i in (Solver.DimYValue,):  # range(solver.dim_y):
            Out += Cls.ShowSpecial(Solver, i)
            Out += "\n\n\n"
        with open(Solver.OutputValue, 'w', encoding='utf-8') as Fileout:
            Fileout.write(Out)
        return Out
