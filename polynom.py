from scipy import special
import numpy as np


class Polynomial:
    def __init__(Self, PolynomialType):
        # Обираємо поліном для розрахунку коефіцієнтів згідно з налаштуваннями.
        if PolynomialType == "Чебишева":
            Self.GetCoefficients = lambda n: np.array(special.chebyt(n).coefficients)
        elif PolynomialType == "Лежандра":
            Self.GetCoefficients = lambda n: np.array(special.legendre(n).coefficients)
        elif PolynomialType == "Лагерра":
            Self.GetCoefficients = lambda n: np.array(special.laguerre(n).coefficients)
        elif PolynomialType == "Ерміта":
            Self.GetCoefficients = lambda n: np.array(special.hermite(n).coefficients)
        else:
            exit("Polynomial type is not defined!")

    def GetPolynomialSumCoefficients(Self, Degree, PolynomialMultiplier=None):
        """Повертає коефіцієнти суми полиномів степенів від 0 до degree включно."""
        if PolynomialMultiplier is None:
            PolynomialMultiplier = np.ones(Degree+1)
        PolynomialSumCoefficients = np.zeros(Degree+1)
        for Deg in np.arange(Degree+1):
            # Обраховуємо коефіцієнти полиному потрібного степеню.
            Polynomial = Self.GetCoefficients(Deg) * PolynomialMultiplier[Deg]
            # Сумуємо коефіцієнты полінома потрібного степеню з коефіцієнтами попередніх поліномів.
            for Position in np.arange(1, Deg+2):
                PolynomialSumCoefficients[-Position] += Polynomial[-Position]
        return np.flipud(PolynomialSumCoefficients)
