import matplotlib.pyplot as plt
import numpy as np
from calculations import Solve


class Graph:
    def __init__(Self, Ui):
        Solver = Solve(Ui)
        Self.PlotNormalized = Self.IsNormalized(Solver.PlotNormalizedValue)
        Self.Estimate = Self.GetEstimate(Solver)
        Self.Error = Self.GetError(Solver)
        Self.Y = Self.GetY(Solver)
        Self.SampleSize = Solver.SampleSizeValue

    @staticmethod
    def GetY(Solver):
        if Solver.PlotNormalizedValue:
            return Solver.YNormalized
        else:
            return Solver.Y

    @staticmethod
    def IsNormalized(PlotNormalized):
        """Повертає True, якщо потрібно зробити нормалізований графік."""
        return PlotNormalized

    def GetEstimate(Self, Solver):
        """Повертає стовпець наближень у в залежності від налаштувань."""
        if Self.PlotNormalized:
            return Solver.EstimateNormalized
        else:
            return Solver.Estimate

    def GetError(self, solver):
        """Повертає похибку (нормалізовану чи звичайну)."""
        if self.PlotNormalized:
            return solver.ErrorNormalized
        else:
            return solver.Error

    def PlotGraph(self):
        samples = np.arange(1, self.SampleSize + 1)
        number_of_graphs = self.Error.size
        fig, axes = plt.subplots(2, number_of_graphs, squeeze=False, figsize=(12, 8))
        fig.suptitle('Графіки оцінок та похибок', fontsize=18, fontweight='bold')

        for i in np.arange(number_of_graphs):
            # Верхний график: исходные данные и оценка
            axes[0][i].plot(samples, self.Y[i], label=f'Y{i + 1}', color='#1f77b4', linewidth=2, marker='o')
            axes[0][i].plot(samples, self.Estimate[i], linestyle='--', label=f'Ф{i + 1}', color='#ff7f0e', linewidth=2,
                            marker='x')
            axes[0][i].set_title(f"Похибка: {self.Error[i]:.4f}", fontsize=14, fontweight='bold')
            axes[0][i].legend(loc='upper right')
            axes[0][i].grid(True, which='both', linestyle='--', linewidth=0.5)
            axes[0][i].set_xlabel('Зразки', fontsize=12)
            axes[0][i].set_ylabel('Значення', fontsize=12)
            axes[0][i].tick_params(axis='both', which='major', labelsize=10)
            axes[0][i].tick_params(axis='both', which='minor', labelsize=8)

            # Нижний график: абсолютная ошибка
            axes[1][i].plot(samples, np.abs(self.Y[i] - self.Estimate[i]), label='Похибка', color='#d62728',
                            linewidth=2, marker='s')
            axes[1][i].legend(loc='upper right')
            axes[1][i].grid(True, which='both', linestyle='--', linewidth=0.5)
            axes[1][i].set_xlabel('Зразки', fontsize=12)
            axes[1][i].set_ylabel('Абсолютна похибка', fontsize=12)
            axes[1][i].tick_params(axis='both', which='major', labelsize=10)
            axes[1][i].tick_params(axis='both', which='minor', labelsize=8)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()
