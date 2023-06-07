from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import math as mth
from lab1_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from time import sleep
from random import randint


matplotlib.use("Qt5Agg")

def render_apple(x, y, width=0.25):
    return [
        x + width,
        x + width,
        x - width,
        x - width,
        x + width
    ], [
        y + width,
        y - width,
        y - width,
        y + width,
        y + width
    ]

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
        self.ui.spinBox_X.valueChanged.connect(self.reset)
        self.ui.spinBox_Y.valueChanged.connect(self.reset)
        self._length = 15
        self.show_plot()
        self._apple_pos = (self.return_apple())
        self._stopped = False

    def reset(self):
        self._values = ([], [])
        self.ui.MplWidget.canvas.axes.clear()
        self._apple_pos = (self.return_apple())
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
        rad = round((-((self.ui.dial.value() + 250) %
                    1000)) / 1000 * 4)/2 * mth.pi
        val = self.get_values()
        max_x = self.ui.spinBox_X.value()
        new_x = round(mth.cos(rad) + (val[0][-1] if len(val[0]) > 0 else 0))
        new_x = 0 if new_x < 0 else min(new_x, max_x)
        max_y = self.ui.spinBox_Y.value()
        new_y = round(mth.sin(rad) + (val[1][-1] if len(val[1]) > 0 else 0))
        new_y = 0 if new_y < 0 else min(new_y, max_y)
        return (new_x, new_y)

    def return_apple(self):
        x = randint(0, self.ui.spinBox_X.value())
        y = randint(0, self.ui.spinBox_Y.value())
        return [x, x], [y, y]

    def apple_coll(self):
        val = self._values
        x = val[0][-1]
        y = val[1][-1]
        if (abs(x - self._apple_pos[0][0]) <= 1 and
                abs(y - self._apple_pos[1][0]) <= 1):
            return True
        else:
            return False

    def write_point(self):
        x, y = self.next_coord()
        val = self.get_values()
        self._values[0].append(x)
        self._values[1].append(y)
        if (self.apple_coll()):
            self._length += 3
            self._apple_pos = self.return_apple()
        if (len(val[0]) > self._length):
            del val[0][0]
            del val[1][0]
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(
            val[0], val[1], 'g', linewidth=5)
        self.ui.MplWidget.canvas.axes.plot(
            self._apple_pos[0], self._apple_pos[1], 'or', linewidth=1000)
        self.show_plot()
        if (self._stopped):
            exit()
        if (x, y) in zip(val[0][0: -1], val[1][0: -1]):
            self._stopped = True
        self.timer.start(10)

    def mybuttonfunction(self):
        if self.timer.remainingTime() > 0:
            self.timer.stop()
        else:
            self.timer.start(10)


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
