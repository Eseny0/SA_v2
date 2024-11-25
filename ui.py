from PySide6 import QtCore, QtWidgets  # Імпорт основних бібліотек для Qt
from PySide6.QtGui import QFont  # Імпорт для роботи з шрифтами


# Клас для побудови інтерфейсу головного вікна
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)  # Встановлення розміру вікна
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))  # Мінімальний розмір вікна
        MainWindow.setMaximumSize(QtCore.QSize(1300, 782))  # Максимальний розмір вікна
        MainWindow.setAcceptDrops(False)  # Заборона перетягування файлів у вікно

        # Створення центрального віджета
        self.СentralWidget = QtWidgets.QWidget(MainWindow)
        self.СentralWidget.setObjectName("CentralWidget")

        # Блок для вводу даних
        self.InputBlock = QtWidgets.QGroupBox(self.СentralWidget)
        self.InputBlock.setGeometry(QtCore.QRect(20, 70, 1160, 230))
        self.InputBlock.setObjectName("InputBlock")

        # Блок для кнопок
        self.ButtonsBlock = QtWidgets.QGroupBox(self.СentralWidget)
        self.ButtonsBlock.setGeometry(QtCore.QRect(20, 10, 1160, 60))
        self.ButtonsBlock.setObjectName("ButtonsBlock")

        # Блок для виводу результатів
        self.OutputBlock = QtWidgets.QTextBrowser(self.СentralWidget)
        self.OutputBlock.setGeometry(QtCore.QRect(20, 310, 1160, 370))
        self.OutputBlock.setStyleSheet("background-color: #313131; color: white;")
        self.OutputBlock.setObjectName("OutputBlock")

        # Поле для вводу шляху вхідного файлу
        self.InputFileTxt = QtWidgets.QLineEdit(self.InputBlock)
        self.InputFileTxt.setGeometry(QtCore.QRect(300, 190, 200, 22))
        self.InputFileTxt.setDragEnabled(False)
        self.InputFileTxt.setObjectName("InputFileTxt")

        # Кнопка для вибору вхідного файлу
        self.InputFileButton = QtWidgets.QToolButton(self.InputBlock)
        self.InputFileButton.setGeometry(QtCore.QRect(510, 190, 60, 22))
        self.InputFileButton.setObjectName("InputFileButton")

        # Поле вводу для вихідного файлу
        self.OutputFileTxt = QtWidgets.QLineEdit(self.InputBlock)
        self.OutputFileTxt.setGeometry(QtCore.QRect(645, 190, 200, 22)) 
        self.OutputFileTxt.setObjectName("OutputFileTxt")

        # Кнопка для вибору вихідного файлу
        self.OutputFileButton = QtWidgets.QToolButton(self.InputBlock)
        self.OutputFileButton.setGeometry(QtCore.QRect(855, 190, 60, 22))
        self.OutputFileButton.setObjectName("OutputFileButton")

        # Мітка для тексту "Розмір вибірки"
        self.SampleSizeTxt = QtWidgets.QLabel(self.InputBlock)
        self.SampleSizeTxt.setGeometry(QtCore.QRect(100, 70, 115, 22))
        self.SampleSizeTxt.setObjectName("SampleSizeTxt")

        # Поле для введення розміру вибірки
        self.SampleSizeButton = QtWidgets.QSpinBox(self.InputBlock)
        self.SampleSizeButton.setAlignment(QtCore.Qt.AlignCenter)
        self.SampleSizeButton.setGeometry(QtCore.QRect(225, 70, 40, 22))
        self.SampleSizeButton.setMouseTracking(False)
        self.SampleSizeButton.setMinimum(1)
        self.SampleSizeButton.setMaximum(100)
        self.SampleSizeButton.setObjectName("SampleSizeButton")

        # Мітка для тексту "Розмірності векторів"
        self.VectorsSizeTxt = QtWidgets.QLabel(self.InputBlock)
        self.VectorsSizeTxt.setGeometry(QtCore.QRect(400, 70, 150, 22))
        self.VectorsSizeTxt.setObjectName("VectorsSizeTxt")

        # Мітка для тексту "Розмірність вектора X1"
        self.VectorX1Txt = QtWidgets.QLabel(self.InputBlock)
        self.VectorX1Txt.setGeometry(QtCore.QRect(560, 70, 35, 22))
        self.VectorX1Txt.setObjectName("VectorX1Txt")

        # Поле для введення розміру вектора X1
        self.VectorX1Button = QtWidgets.QSpinBox(self.InputBlock)
        self.VectorX1Button.setAlignment(QtCore.Qt.AlignCenter)
        self.VectorX1Button.setGeometry(QtCore.QRect(590, 70, 40, 22))
        self.VectorX1Button.setMouseTracking(False)
        self.VectorX1Button.setMinimum(1)
        self.VectorX1Button.setObjectName("VectorX1Button")

        # Мітка для тексту "Розмірність вектора X2"
        self.VectorX2Txt = QtWidgets.QLabel(self.InputBlock)
        self.VectorX2Txt.setGeometry(QtCore.QRect(690, 70, 35, 22))
        self.VectorX2Txt.setObjectName("VectorX2Txt")

        # Поле вводу для значення вектора X2
        self.VectorX2Button = QtWidgets.QSpinBox(self.InputBlock)  
        self.VectorX2Button.setAlignment(QtCore.Qt.AlignCenter)
        self.VectorX2Button.setGeometry(QtCore.QRect(720, 70, 40, 22))
        self.VectorX2Button.setMinimum(1)
        self.VectorX2Button.setObjectName("VectorX2Button")

        # Текстова мітка для вектора X3
        self.VectorX3Txt = QtWidgets.QLabel(self.InputBlock)
        self.VectorX3Txt.setGeometry(QtCore.QRect(820, 70, 35, 22))
        self.VectorX3Txt.setObjectName("VectorX3Txt")
        
        # Поле вводу для значення вектора X3
        self.VectorX3Button = QtWidgets.QSpinBox(self.InputBlock)
        self.VectorX3Button.setAlignment(QtCore.Qt.AlignCenter)
        self.VectorX3Button.setGeometry(QtCore.QRect(850, 70, 40, 22))
        self.VectorX3Button.setMinimum(1)
        self.VectorX3Button.setObjectName("VectorX3Button")

        # Текстова мітка для вектора Y
        self.VectorYTxt = QtWidgets.QLabel(self.InputBlock)
        self.VectorYTxt.setGeometry(QtCore.QRect(950, 70, 30, 22))
        self.VectorYTxt.setObjectName("VectorYTxt")

        # Поле вводу для значення вектора Y
        self.VectorYButton = QtWidgets.QSpinBox(self.InputBlock)
        self.VectorYButton.setAlignment(QtCore.Qt.AlignCenter)
        self.VectorYButton.setGeometry(QtCore.QRect(980, 70, 40, 22))
        self.VectorYButton.setMinimum(1)
        self.VectorYButton.setObjectName("VectorYButton")

        # Текст тип полінома
        self.PolynomTxt = QtWidgets.QLabel(self.InputBlock)  
        self.PolynomTxt.setGeometry(QtCore.QRect(110, 100, 105, 22))
        self.PolynomTxt.setObjectName("PolynomTxt")

        # Кнопка тип полінома
        self.PolynomButton = QtWidgets.QComboBox(self.InputBlock)  
        self.PolynomButton.setGeometry(QtCore.QRect(225, 100, 120, 22))
        self.PolynomButton.setObjectName("PolynomButton")

        # Текст степені поліномів
        self.PolynomsDegreesTxt = QtWidgets.QLabel(self.InputBlock)  
        self.PolynomsDegreesTxt.setGeometry(QtCore.QRect(400, 100, 130, 22))
        self.PolynomsDegreesTxt.setObjectName("PolynomsDegreesTxt")

        # Текст степінь полінома х1
        self.PolynomDegreeX1Txt = QtWidgets.QLabel(self.InputBlock)  
        self.PolynomDegreeX1Txt.setGeometry(QtCore.QRect(560, 100, 35, 22))
        self.PolynomDegreeX1Txt.setObjectName("PolynomDegreeX1Txt")

        # Кнопка степінь полінома х1
        self.X1DegreeButton = QtWidgets.QSpinBox(self.InputBlock)  
        self.X1DegreeButton.setAlignment(QtCore.Qt.AlignCenter)
        self.X1DegreeButton.setGeometry(QtCore.QRect(590, 100, 40, 22))
        self.X1DegreeButton.setMouseTracking(False)
        self.X1DegreeButton.setMinimum(1)
        self.X1DegreeButton.setObjectName("X1DegreeButton")

        # Текст степінь полінома х2
        self.PolynomDegreeX2Txt = QtWidgets.QLabel(self.InputBlock)  
        self.PolynomDegreeX2Txt.setGeometry(QtCore.QRect(690, 100, 35, 22))
        self.PolynomDegreeX2Txt.setObjectName("PolynomDegreeX2Txt")

        # Кнопка степінь полінома х2
        self.X2DegreeButton = QtWidgets.QSpinBox(self.InputBlock)  
        self.X2DegreeButton.setAlignment(QtCore.Qt.AlignCenter)
        self.X2DegreeButton.setGeometry(QtCore.QRect(720, 100, 40, 22))
        self.X2DegreeButton.setMinimum(1)
        self.X2DegreeButton.setObjectName("X2DegreeButton")

        # Текст степінь полінома х3
        self.PolynomDegreeX3Txt = QtWidgets.QLabel(self.InputBlock)  
        self.PolynomDegreeX3Txt.setGeometry(QtCore.QRect(820, 100, 35, 22))
        self.PolynomDegreeX3Txt.setObjectName("PolynomDegreeX3Txt")

        # Кнопка степінь полінома х3
        self.X3DegreeButton = QtWidgets.QSpinBox(self.InputBlock)  
        self.X3DegreeButton.setAlignment(QtCore.Qt.AlignCenter)
        self.X3DegreeButton.setGeometry(QtCore.QRect(850, 100, 40, 22))
        self.X3DegreeButton.setMinimum(1)
        self.X3DegreeButton.setObjectName("X3DegreeButton")

        # Текст ваги цільових функцій
        self.WeightsTxt = QtWidgets.QLabel(self.InputBlock)  
        self.WeightsTxt.setGeometry(QtCore.QRect(55, 130, 160, 22))
        self.WeightsTxt.setObjectName("WeightsTxt")

        # Кнопка ваги цільових функцій
        self.WeightsButton = QtWidgets.QComboBox(self.InputBlock)  
        self.WeightsButton.setGeometry(QtCore.QRect(225, 130, 120, 22))
        self.WeightsButton.setObjectName("WeightsButton")

        # Кнопка лямбда з 3-х систем
        self.LambdaFromThreeSystemsButton = QtWidgets.QCheckBox(self.InputBlock)  
        self.LambdaFromThreeSystemsButton.setGeometry(QtCore.QRect(225, 35, 300, 22))
        self.LambdaFromThreeSystemsButton.setObjectName("LambdaFromThreeSystemsButton")

        # Кнопка нормалізований графік
        self.PlotNomalizedButton = QtWidgets.QCheckBox(self.InputBlock)  
        self.PlotNomalizedButton.setGeometry(QtCore.QRect(675, 35, 170, 22))
        self.PlotNomalizedButton.setObjectName("PlotNomalizedButton")

        # Кнопка для обчислення оптимальних степенів
        self.CalculateOptimalDegreesButton = QtWidgets.QPushButton(self.ButtonsBlock)
        self.CalculateOptimalDegreesButton.setGeometry(QtCore.QRect(150, 30, 300, 25))
        self.CalculateOptimalDegreesButton.setObjectName("CalculateOptimalDegreesButton")
        
        # Кнопка відновити функ залежності
        self.DependenciesButton = QtWidgets.QPushButton(self.ButtonsBlock) 
        self.DependenciesButton.setGeometry(QtCore.QRect(500, 30, 300, 25))
        self.DependenciesButton.setObjectName("DependenciesButton")

        # Кнопка графіка
        self.PlotButton = QtWidgets.QPushButton(self.ButtonsBlock)  
        self.PlotButton.setGeometry(QtCore.QRect(850, 30, 200, 25))
        self.PlotButton.setObjectName("PlotButton")

        # Встановлення центрального віджету
        MainWindow.setCentralWidget(self.СentralWidget)
        self.Statusbar = QtWidgets.QStatusBar(MainWindow)
        self.Statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.Statusbar)

        # Виклик методу для переведення тексту елементів інтерфейсу
        self.retranslateUi(MainWindow)

        # Підключення слотів до сигналів в головному вікні
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate  # Ініціалізація методу перекладу
        # Встановлення заголовка вікна
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab_2_SystemAnalysis"))

        # Встановлення тексту для кнопок та інших елементів інтерфейсу
        self.LambdaFromThreeSystemsButton.setText(_translate("MainWindow", "Визначити лямбда з трьох систем рівнянь"))
        self.PlotNomalizedButton.setText(_translate("MainWindow", "Нормалізувати графік"))
        self.WeightsTxt.setText(_translate("MainWindow", "  Ваги цільових функцій:  "))
        self.PlotButton.setText(_translate("MainWindow", "Побудувати графік"))
        self.InputFileButton.setText(_translate("MainWindow", "Обрати"))
        self.OutputFileButton.setText(_translate("MainWindow", "Обрати"))
        
        # Встановлення тексту підказки для полів вводу файлів
        self.InputFileTxt.setPlaceholderText(_translate("MainWindow", "Вхідний файл"))
        self.InputFileTxt.setAlignment(QtCore.Qt.AlignCenter)  # Центрування тексту
        self.OutputFileTxt.setPlaceholderText(_translate("MainWindow", "Вихідний файл"))
        self.OutputFileTxt.setAlignment(QtCore.Qt.AlignCenter)  # Центрування тексту

        # Встановлення тексту для міток розміру вибірки та векторів
        self.SampleSizeTxt.setText(_translate("MainWindow", "  Розмір вибірки:  "))
        self.VectorX2Txt.setText(_translate("MainWindow", "  Х2:  "))
        self.VectorX3Txt.setText(_translate("MainWindow", "  Х3:  "))
        self.VectorX1Txt.setText(_translate("MainWindow", "  Х1:  "))
        self.VectorYTxt.setText(_translate("MainWindow", "  Y:  "))
        self.VectorsSizeTxt.setText(_translate("MainWindow", "  Розмірності векторів:  "))

        # Встановлення тексту для кнопки відновлення функціональних залежностей
        self.DependenciesButton.setText(_translate("MainWindow", "Відновити функціональні залежності"))

        # Встановлення тексту для поліномів
        self.PolynomTxt.setText(_translate("MainWindow", "  Тип полінома:  "))
        self.PolynomDegreeX1Txt.setText(_translate("MainWindow", "  Х1:  "))
        self.PolynomDegreeX2Txt.setText(_translate("MainWindow", "  Х2:  "))
        self.PolynomsDegreesTxt.setText(_translate("MainWindow", "  Степені поліномів:  "))
        self.PolynomDegreeX3Txt.setText(_translate("MainWindow", "  Х3:  "))

        # Встановлення тексту для кнопки обчислення оптимальних ступенів поліномів
        self.CalculateOptimalDegreesButton.setText(_translate("MainWindow", "Обрахувати оптимальні степені поліномів"))
