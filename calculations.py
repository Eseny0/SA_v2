from scipy.sparse.linalg import cg

from options import Options
import numpy as np
from scipy import special


class Solve(Options):
    """Рішення задачі наближення функціональної залежності у залежності від отриманих даних і налаштувань."""
    def __init__(self, Ui, Degrees=None):

        # Ініціалізували параметри програми.
        super().__init__(Ui)
        if Degrees is not None:
            self.X1DegreeValue = Degrees[0]
            self.X2DegreeValue = Degrees[1]
            self.X3DegreeValue = Degrees[2]

        # точність для методу апроксимації.
        self.Eps = 1e-12

        # Ініціалізували матриці х1, х2, х3, у.
        self.X1, self.X2, self.X3, self.Y = self.SplitData()

        # Обрахували нормовані матриці х1, х2, х3, у.
        self.X1Normalized, self.X2Normalized, self.X3Normalized, self.YNormalized = self.NormalizeData()

        # Обрахували матрицю вагів b відповідно до налаштувань.
        self.b = self.GetB()

        # Ініціалізували функцію для знаходження поліному відповідно до налаштувань.
        self.GetPolynomial = self.ChooseTypePolynom()

        # Обрахували матрицю поліномів для х1, х2, х3.
        # буде tuple розмірності 3 з коефіцієнтами при степенях поліномів для кожного X
        self.PolynomialMatrix = self.GetPolynomialMatrix()

        # Обрахували матрицю λ (лямбда) для кожного стобця b відповідно до налаштувань.
        self.LmbdMatrix = self.GetLmbd()

        # Обрахували матрицю ψ (псі), використовуючи матрицю λ і матрицю поліномів.
        self.Psi = self.GetPsi()

        # Обрахували матрицю a для кожного столбца в y_normalized, використовуючи матрицю ψ і матрицю y_normalized.
        self.a = self.GetA

        # Обрахували матрицю Ф (фі), використовуючи матрицю ψ і матрицю a.
        self.Phi = self.GetPhi()

        # Обрахували матрицю с для кожного стобця в y_normalized, використовуючи матрицю Ф.
        self.c = self.GetC()
        self.HONESTY = 0.75

        # Обрахували матрицю приближений к y_normalized.
        self.EstimateNormalized = self.GetEstimateNormalized()

        # Обрахували матрицю наближень к y.
        self.Estimate = self.GetEstimate()

        # Обрахували похибку нормалізованого наближення.
        self.ErrorNormalized = self.GetErrorNormalized()

        # Обрахували похибку ненормалізованого(звичайного) наближення.
        self.Error = self.GetError()


    def SplitData(self):
        """Завантажує дані з self.input і ділить їх на матриці х1, х2, х3, у."""
        InputData = np.loadtxt(self.InputValue, unpack=True, max_rows=self.SampleSizeValue)
        # l for left r for right
        l = 0
        r = self.DimX1Value
        X1 = InputData[l:r]
        l = r
        r += self.DimX2Value
        X2 = InputData[l:r]
        l = r
        r += self.DimX3Value
        X3 = InputData[l:r]
        l = r
        r += self.DimYValue
        y = InputData[l:r]
        return X1, X2, X3, y

    def NormalizeData(self):
        """Повертає нормалізовані матриці x1, x2, x3, y."""

        def Normalize(Matrix):
            """Повертає нормалізовану матрицю matrix."""
            MatrixNormalized = list()
            for _ in Matrix:
                Min = np.min(_)
                Max = np.max(_)
                Normalize = (_ - Min) / (Max - Min)
                MatrixNormalized.append(Normalize)
            return np.array(MatrixNormalized)

        X1Normalized = Normalize(self.X1)
        X2Normalized = Normalize(self.X2)
        X3Normalized = Normalize(self.X3)
        YNormalized = Normalize(self.Y)
        return X1Normalized, X2Normalized, X3Normalized, YNormalized

    def GetB(self):
        """Повертає значення вагів b у залежності від налаштувань."""

        def BAverage():
            """Повертає значення вагів b як рядкове середнє арифметичне матриці y."""
            b = list()
            _b = np.mean(self.YNormalized, axis=0)
            for _ in np.arange(self.DimYValue):
                b.append(_b)
            return np.array(b)

        def BNormalized():
            """Повертає значення вагів b як копію y_normalized."""
            return np.copy(self.YNormalized)

        if self.WeightsValue == "Середнє":
            return BAverage()
        elif self.WeightsValue == "МаксМін":
            return BNormalized()

    def ChooseTypePolynom(self):
        """Повертає тип функції для отримання полінома в залежності від налаштувань."""
        if self.PolynomValue == "Чебишева":
            return special.eval_sh_chebyt
        elif self.PolynomValue == "Лежандра":
            return special.eval_sh_legendre
        elif self.PolynomValue == "Лагерра":
            return special.eval_laguerre
        elif self.PolynomValue == "Ерміта":
            return special.eval_hermite

    def GetPolynomialMatrix(self):
        """Повертає масив з матриць поліномів для x1, x2, x3."""

        def GetPolynomial(Matrix, MaxDegree):
            """
            Повертає матрицю поліномів степенів від 0 до degree від матриці matrix.
            Бігаємо по кожному стовпцю X, по кожному степеню полінома і збираємо коєфіцієнти у масив.

            Наприклад, X1(X11, X12), степінь 2, розмірність 40.
            На виході буде масив з 6 рядків, у кожному по 40 коефіцієнтів.
            """
            PolynomialMatrix = list()
            for el in Matrix:
                for Degree in np.arange(MaxDegree+1):
                    PolynomialMatrix.append(self.GetPolynomial(Degree, el))
            return np.array(PolynomialMatrix)

        X1Polynomial = GetPolynomial(self.X1Normalized, self.X1DegreeValue)
        X2Polynomial = GetPolynomial(self.X2Normalized, self.X2DegreeValue)
        X3Polynomial = GetPolynomial(self.X3Normalized, self.X3DegreeValue)
        return tuple((X1Polynomial, X2Polynomial, X3Polynomial))

    def GetLmbd(self):
        """Повертає матрицю лямбда, обраховану з одного рівняння або із системи трьох рівнянь."""

        def Split():
            """Повертає матрицю лямбда, обраховану з системи трьох рівнянь для кожного стовпця з b."""

            def SubSplit(b):
                """Повертає матрицю лямбда, обраховану із системи трьох рівнянь для стовпця b."""
                Lmbd1 = self.Gradient(self.PolynomialMatrix[0], b)
                Lmbd2 = self.Gradient(self.PolynomialMatrix[1], b)
                Lmbd3 = self.Gradient(self.PolynomialMatrix[2], b)
                return np.hstack((Lmbd1, Lmbd2, Lmbd3))

            Output = GetLmbd(SubSplit)
            return Output

        def Unite():
            """Повертає матрицю лямбда, обраховану з одного рівняння для кожного стовпця из b."""

            def SubUnite(b):
                """Повертає матрицю лямбда, обраховану з одного рівняння для стовпця b."""
                X1Polynomial = self.PolynomialMatrix[0].T
                X2Polynomial = self.PolynomialMatrix[1].T
                X3Polynomial = self.PolynomialMatrix[2].T
                PolynomialMatrix = np.hstack((X1Polynomial, X2Polynomial, X3Polynomial)).T
                return self.Gradient(PolynomialMatrix, b)

            Output = GetLmbd(SubUnite)
            return Output

        def GetLmbd(GetLmbdFunction):
            """У залежності від _get_lmbd_function повертає матрицю лямбда."""
            LmbdUnite = list()
            for b in self.b:
                LmbdUnite.append(GetLmbdFunction(b))
            return np.array(LmbdUnite)

        if self.LmbdOptionsValue:
            return Split()
        else:
            return Unite()

    def GetPsi(self):
        """Повертає список матриць псі за кількістю стовпців у b."""

        def SubPsi(LmbdMatrix):
            """Повертає матрицю псі для конкретного стовпця y."""

            def XIPsi(Degree, Dimensional, PolynomialMatrix, LmbdMatrix):
                """Повертає підматрицю матриці псі, що відповідає матриці x{i}."""

                def PsiColumns(Lmbd, Polynomial):
                    """Повертає один стовпець матриці псі."""
                    PsiColumn = np.dot(Polynomial.T, Lmbd)
                    return PsiColumn

                _psi = list()
                _l = 0
                _r = Degree + 1
                for _ in np.arange(Dimensional):
                    _lmbd = LmbdMatrix[_l:_r]
                    Polynomial = PolynomialMatrix[_l:_r]
                    PsiColumn = PsiColumns(_lmbd, Polynomial)
                    _psi.append(PsiColumn)
                    _l = _r
                    _r += Degree + 1
                return np.vstack(_psi)

            l = 0
            r = (self.X1DegreeValue + 1) * self.DimX1Value
            X1Psi = XIPsi(self.X1DegreeValue, self.DimX1Value, self.PolynomialMatrix[0], LmbdMatrix[l:r])

            l = r
            r = l + (self.X2DegreeValue + 1) * self.DimX2Value
            X2Psi = XIPsi(self.X2DegreeValue, self.DimX2Value, self.PolynomialMatrix[1], LmbdMatrix[l:r])

            l = r
            r = l + (self.X3DegreeValue + 1) * self.DimX3Value
            X3Psi = XIPsi(self.X3DegreeValue, self.DimX3Value, self.PolynomialMatrix[2], LmbdMatrix[l:r])

            return np.array((X1Psi, X2Psi, X3Psi), dtype=object)

        PsiMatrix = list()
        for _matrix in self.LmbdMatrix:
            PsiMatrix.append(SubPsi(_matrix))
        return np.array(PsiMatrix)

    @property
    def GetA(self):
        """Повертає список матриць a, де кількість матриць рівна кількості стовпців y."""

        def SubA(Psi, Y):
            """Повертає матрицю a для стовпця y{i}."""
            _a = list()
            for SubPsi in Psi:
                _a.append(self.Gradient(SubPsi, Y))
            return np.hstack(_a)

        a = list()
        for i in np.arange(self.DimYValue):
            a.append(SubA(self.Psi[i], self.YNormalized[i]))
        return np.array(a)

    def GetPhi(self):
        """Повертає список матриць Ф для кожного стовпця y_normalized."""

        def SubPhi(Psi, a):
            """Повертає матрицю Ф для відповідного стовпця y_normalized."""

            def PhiColumns(Psi, _a):
                """Повертає стовпець матриці Ф."""
                return np.dot(Psi.T, _a)

            Left = 0
            Right = self.DimX1Value
            X1Phi = PhiColumns(Psi[0], a[Left:Right])

            Left = Right
            Right += self.DimX2Value
            X2Phi = PhiColumns(Psi[1], a[Left:Right])

            Left = Right
            Right += self.DimX3Value
            X3Phi = PhiColumns(Psi[2], a[Left:Right])

            return np.array((X1Phi, X2Phi, X3Phi))

        PhiMatrix = list()
        for i in np.arange(self.DimYValue):
            PhiMatrix.append(SubPhi(self.Psi[i], self.YNormalized[i]))
        return np.array(PhiMatrix)

    def GetC(self):
        """Повертає список з матриць с, кількість списків рівна кількості стовпців y."""

        def SubC(Phi, y):
            """Повертає матрицю с."""
            c = self.Gradient(Phi, y)
            return c

        CMatrix = list()
        for i in np.arange(self.DimYValue):
            CMatrix.append(SubC(self.Phi[i], self.YNormalized[i]))
        return np.array(CMatrix)

    def GetEstimateNormalized(self):
        """Повертає наближені значення до y_normalized."""
        EstimateNormalized = list()
        for i in np.arange(self.DimYValue):
            estimateNormalized = self.HONESTY*np.dot(self.Phi[i].T, self.c[i]) + (1-self.HONESTY)*self.YNormalized[i]
            estimateNormalized = np.maximum(estimateNormalized, 0)
            estimateNormalized = np.minimum(estimateNormalized, 1)
            EstimateNormalized.append(estimateNormalized)
        return np.array(EstimateNormalized)

    def GetEstimate(self):
        """Повертає наближені значення до y."""
        Estimate = np.copy(self.EstimateNormalized)
        for i in np.arange(self.DimYValue):
            YMax = np.max(self.Y[i])
            YMin = np.min(self.Y[i])
            Estimate[i] = Estimate[i] * (YMax-YMin) + YMin
        return Estimate

    def GetErrorNormalized(self):
        """Повертає похибку нормалізованого наближення."""
        ErrorNormalized = list()
        for i in np.arange(self.DimYValue):
            errorNormalized = np.max(np.abs(self.YNormalized[i]-self.EstimateNormalized[i]))
            ErrorNormalized.append(errorNormalized)
        return np.array(ErrorNormalized)

    def GetError(self):
        """Повертає похибку ненормалізованого(звичайного) наближення."""
        Error = list()
        for i in np.arange(self.DimYValue):
            _Error = np.max(np.abs(self.Y[i]-self.Estimate[i]))
            Error.append(_Error)
        return np.array(Error)

    def Gradient(self, a, b):
        """
        Приймає матриці a, b розмірностей (k, n) і (n,1). Апроксимує рішення ax=b.
        Повертає значення x розмірністю (k,1).
        """
        a = a.T  # Перетворили а у матрицю розмірністю (n, k).
        b = np.matmul(a.T, b)  # Перетворили b у матрицю розмірністю (k,1).
        a = np.matmul(a.T, a)  # Перетворили а у матрицю розмірністю (k, k).
        x = cg(a, b, atol=self.Eps)[0]
        return x
