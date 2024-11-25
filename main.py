import sys
from PySide6 import QtWidgets, QtGui
from ui import Ui_MainWindow
from calculations import Solve
from output import Output
from graphics import Graph
from degrees import GetAutoDegree


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('styles/img/arrow-up.png'))

        # Додаємо елементи в списки для вибору поліномів та ваг
        self.PolynomButton.addItems(["Чебишева", "Лежандра", "Лагерра", "Ерміта"])
        self.WeightsButton.addItems(["Середнє", "МаксМін"])

        # Підключаємо кнопки до відповідних функцій
        self.InputFileButton.clicked.connect(self.ChooseInput)  # Вибір вхідного файлу
        self.OutputFileButton.clicked.connect(self.ChooseOutput)  # Вибір вихідного файлу
        self.DependenciesButton.clicked.connect(self.Execute)  # Виконання обчислень
        self.PlotButton.clicked.connect(self.Plot)  # Побудова графіка
        self.CalculateOptimalDegreesButton.clicked.connect(self.AutoDegree)  # Авто-оцінка степенів полінома

        # Встановлюємо початкові значення для полів вводу
        self.VectorX1Button.setValue(2)
        self.VectorX2Button.setValue(2)
        self.VectorX3Button.setValue(3)
        self.VectorYButton.setValue(4)
        self.SampleSizeButton.setValue(45)
        self.X1DegreeButton.setValue(3)
        self.X2DegreeButton.setValue(3)
        self.X3DegreeButton.setValue(3)

    def ChooseInput(self):
        # Вибір вхідного файлу для обробки
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open data file', '.', 'Data file (*.txt)')[0]
        self.InputFileTxt.setText(filename)

    def ChooseOutput(self):
        # Вибір вихідного файлу для збереження результатів
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open data file', '.', 'Data file (*.txt)')[0]
        self.OutputFileTxt.setText(filename)

    def Execute(self):
        # Виконує обчислення на основі вхідних даних
        self.DependenciesButton.setEnabled(False)  # Вимикає кнопку на час виконання
        solver = Solve(self)
        self.OutputBlock.setText(Output.show(solver))  # Відображення результату
        self.DependenciesButton.setEnabled(True)  # Увімкнення кнопки після виконання

    def Plot(self):
        """Відмальовка графіка."""
        self.PlotButton.setEnabled(False)  # Вимикає кнопку на час побудови графіка
        plotter = Graph(self)
        plotter.PlotGraph()  # Викликає функцію для побудови графіка
        self.PlotButton.setEnabled(True)  # Увімкнення кнопки після завершення

    def AutoDegree(Self):
        """Оцінка оптимальних степенів полінома."""
        Self.CalculateOptimalDegreesButton.setEnabled(False)  # Вимикає кнопку на час обчислення
        Degrees = GetAutoDegree(Self)
        # Відображає оптимальні степені для поліномів
        Self.OutputBlock.setText(f"Оптимальні степені поліномів:\nX1: {Degrees[0]}\nX2: {Degrees[1]}\nX3: {Degrees[2]}")
        Self.CalculateOptimalDegreesButton.setEnabled(True)  # Увімкнення кнопки після завершення

# Функція для завантаження стилю з QSS файлу
def LoadStylesheet(path):
    try:
        with open(path, 'r') as file:
            stylesheet = file.read()
            return stylesheet
    except FileNotFoundError:
        print(f"File {path} not found.")  # Виводить повідомлення, якщо файл стилю не знайдено
        return ""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UI()

    # Завантажуємо стиль з QSS файлу
    qss_path = "styles/Darkeum.qss"
    qss = LoadStylesheet(qss_path)
    if qss:
        app.setStyleSheet(qss)  # Встановлюємо стиль для додатку

    MainWindow.show()  # Показуємо головне вікно

    sys.exit(app.exec())  # Запускаємо додаток
