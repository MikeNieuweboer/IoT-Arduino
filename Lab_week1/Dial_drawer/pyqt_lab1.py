from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import math as mth
from lab1_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


matplotlib.use("Qt5Agg")


class Lab1(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Dial drawer")
        self.ui.pushButton.clicked.connect(self.mybuttonfunction)
        self.timer = QTimer()
        self.timer.timeout.connect(self.write_point)
        self._values = ([], [])
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.spinBox_X.valueChanged.connect(self.show_plot)
        self.ui.spinBox_Y.valueChanged.connect(self.show_plot)
        self.show_plot()

    def reset(self):
        self._values = ([], [])
        self.ui.MplWidget.canvas.axes.clear()
        self.show_plot()

    def show_plot(self):
        max_x = self.ui.spinBox_X.value()
        max_y = self.ui.spinBox_Y.value()
        self.ui.MplWidget.canvas.axes.set_xlim((-0.1, max_x + 0.1))
        self.ui.MplWidget.canvas.axes.set_ylim((-0.1, max_y + 0.1))
        self.ui.MplWidget.canvas.draw()

    def get_values(self):
        return self._values

    def next_coord(self):
        rad = (-((self.ui.dial.value() + 250) % 1000)) / 1000 * 2 * mth.pi
        val = self.get_values()
        max_x = self.ui.spinBox_X.value()
        new_x = mth.cos(rad) + (val[0][-1] if len(val[0]) > 0 else 0)
        new_x = 0 if new_x < 0 else min(new_x, max_x)
        max_y = self.ui.spinBox_Y.value()
        new_y = mth.sin(rad) + (val[1][-1] if len(val[1]) > 0 else 0)
        new_y = 0 if new_y < 0 else min(new_y, max_y)
        return (new_x, new_y)

    def write_point(self):
        x, y = self.next_coord()
        self._values[0].append(x)
        self._values[1].append(y)
        val = self.get_values()
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(
            val[0], val[1], 'r', linewidth=0.5)
        self.show_plot()
        self.timer.start(100)

    def mybuttonfunction(self):
        if self.timer.remainingTime() > 0:
            self.timer.stop()
        else:
            self.timer.start(100)


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
