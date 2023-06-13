# Poject: Lab1_task2
# Group: G
# Students: Rob Bieman, Mike Nieuweboer
# Date: 8 juni 2023
#
# Python program to control a pyqt application which plots
# a graph at a given time interval and a given maximum x-value.

import matplotlib
from lab1_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
import sys
from random import randint


matplotlib.use("Qt5Agg")


class Lab1(QMainWindow):
    """
    Class for window object which controls a randomly generated graph, along
    with its different parameters.
    """

    def __init__(self, *args):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("arduino_sensors")
        self.ui.pushButton.clicked.connect(self.start_graph)
        self.timer = QTimer()
        self.timer.timeout.connect(self.write_point)
        self._values = ([0], [0])
        self.ui.pushButton_2.clicked.connect(self.reset)

    def reset(self):
        """
        Clears the plot, stops the timer and removes all points from the
        values list.
        """
        self._values = ([0], [0])
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(
            self._values[0], self._values[1], 'r', linewidth=0.5)
        self.ui.MplWidget.canvas.draw()

    def write_point(self):
        """
        Adds a new semi-random number to the values list and draws the new
        graph. If the graph has reached its maximum x-value, it stops.
        """
        x = len(self._values[0]) + 1
        if (x > self.ui.spinBox_2.value()):
            self._values = ([0], [0])
            self.timer.stop()
            return
        self._values[0].append(x)
        self._values[1].append(
            min(max(0, self._values[1][-1] + randint(-1, 1)), 9))
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(
            self._values[0], self._values[1], 'r', linewidth=0.5)
        self.ui.MplWidget.canvas.axes.set_xlim(0, self.ui.spinBox_2.value())
        self.ui.MplWidget.canvas.axes.set_ylim(0, 10)
        self.ui.MplWidget.canvas.draw()
        self.timer.start(self.ui.spinBox.value())

    def start_graph(self):
        """
        Starts a new timer causing a new graph to be generated. If one is
        being generated, the timer is stopped and the values deleted.
        """
        if self.timer.remainingTime() > 0:
            self.timer.stop()
            self._values = ([0], [0])
        else:
            self.timer.start(self.ui.spinBox.value())


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
