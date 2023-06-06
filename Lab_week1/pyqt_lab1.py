from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import math as mth
from lab1_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from random import randint


matplotlib.use("Qt5Agg")


class Lab1(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("arduino_sensors")
        self.ui.pushButton.clicked.connect(self.mybuttonfunction)
        self.timer = QTimer()
        self.timer.timeout.connect(self.write_point)
        self._values = ([0], [0])
        self.ui.pushButton_2.clicked.connect(self.reset)

    def reset(self):
        self._values = ([], [])
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(
            self._values[0], self._values[1], 'r', linewidth=0.5)
        self.ui.MplWidget.canvas.draw()

    def write_point(self):
        x = len(self._values[0]) + 1
        if (x >= self.ui.spinBox_2.value()):
            self._values = ([], [])
            self.timer.stop()
            return
        self._values[0].append(len(self._values[0]) + 1)
        self._values[1].append(randint(0, self.ui.spinBox.value()))
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(
            self._values[0], self._values[1], 'r', linewidth=0.5)
        self.ui.MplWidget.canvas.axes.set_xlim(0, self.ui.spinBox_2.value())
        self.ui.MplWidget.canvas.draw()
        self.timer.start(120)

    def mybuttonfunction(self):
        if self.timer.remainingTime() > 0:
            self.timer.stop()
        else:
            self.timer.start(120)


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
