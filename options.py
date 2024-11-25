class Options:
    def __init__(Self, Ui):
        Self.InputValue = Self.Input(Ui)
        Self.OutputValue = Self.Output(Ui)
        Self.SampleSizeValue = Self.SampleSize(Ui)
        Self.DimX1Value = Self.DimX1(Ui)
        Self.DimX2Value = Self.DimX2(Ui)
        Self.DimX3Value = Self.DimX3(Ui)
        Self.DimYValue = Self.DimY(Ui)
        Self.PolynomValue = Self.Polynom(Ui)
        Self.X1DegreeValue = Self.D1Degree(Ui)
        Self.X2DegreeValue = Self.X2Degree(Ui)
        Self.X3DegreeValue = Self.X3Degree(Ui)
        Self.WeightsValue = Self.Weights(Ui)
        Self.LmbdOptionsValue = Self.LambdaOptions(Ui)
        Self.PlotNormalizedValue = Self.PlotNormalized(Ui)

    def Input(self, Ui):
        Input = Ui.InputFileTxt.text()
        return Input

    def Output(self, Ui):
        _output = Ui.OutputFileTxt.text()
        return _output

    def SampleSize(self, Ui):
        return Ui.SampleSizeButton.value()

    def DimX1(self, Ui):
        return Ui.VectorX1Button.value()

    def DimX2(self, Ui):
        return Ui.VectorX2Button.value()

    def DimX3(self, Ui):
        return Ui.VectorX3Button.value()

    def DimY(self, Ui):
        return Ui.VectorYButton.value()

    def Polynom(self, Ui):
        return Ui.PolynomButton.currentText()

    def D1Degree(self, Ui):
        return Ui.X1DegreeButton.value()

    def X2Degree(self, Ui):
        return Ui.X2DegreeButton.value()

    def X3Degree(self, Ui):
        return Ui.X3DegreeButton.value()

    def Weights(self, Ui):
        return Ui.WeightsButton.currentText()

    def LambdaOptions(self, Ui):
        return Ui.LambdaFromThreeSystemsButton.isChecked()

    def __what_y_plot(self, Ui):
        return Ui.what_y_plot.value()

    def PlotNormalized(self, Ui):
        return Ui.PlotNomalizedButton.isChecked()
