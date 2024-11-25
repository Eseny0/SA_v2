import numpy as np
from calculations import Solve


def GetAutoDegree(Ui, X1Max=10, X2Max=10, X3Max=10):
    """Методом підбору визначає найбільш оптимальні степені поліномів за критерієм Чебишева."""
    MinDegrees = np.ones(3).astype(int)
    MinError = GetMaxError(Ui, MinDegrees)
    for X1Deg in np.arange(1, X1Max+1):
        for X2Deg in np.arange(1, X2Max+1):
            for X3Deg in np.arange(1, X3Max+1):
                Degrees = np.array((X1Deg, X2Deg, X3Deg)).astype(int)
                CurrentError = GetMaxError(Ui, Degrees)
                if CurrentError < MinError:
                    MinDegrees = np.copy(Degrees)
                    MinError = CurrentError
    return MinDegrees


def GetMaxError(Ui, Degrees):
    """Повертає максимальну похибку за критерієм Чебишева."""
    Solver = Solve(Ui, Degrees)
    return np.max(Solver.ErrorNormalized)
