# Poject: Lab1_task5
# Group: G
# Students: Rob Bieman, Mike Nieuweboer
# Date: 8 juni 2023
#
# Communicates with arduino to get 30 measurements of the accelerometer over
# 15 seconds. Displays the g-forces in the x, y and z axes along with their
# combined values, of which the mean and standard deviation are printed out.
# Uses a worker thread to plot and main thread for UI.

from matplotlib import use as matplotlib_use
from math import sqrt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import sys
from lab1_ui import Ui_Form
import serial


matplotlib_use("Qt5Agg")


class plotter(QObject):
    finished = pyqtSignal()
    mean = pyqtSignal((float, float))

    def __init__(self, canvas):
        self.canvas = canvas
        QObject.__init__(self)
        self.running = True

    def set_style(self, min_x):
        """
        Sets the style of a matplotlib figure which was plotted before this
        function call.
        """
        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Gravitational force (g)")
        self.canvas.axes.set_xticks(range(int(min_x), int(min_x + 9)))
        self.canvas.axes.set_xlim(min_x, min_x + 8)
        self.canvas.axes.legend(loc='upper center', bbox_to_anchor=(
            0.5, -0.12), ncol=3, fancybox=True, shadow=True)
        self.canvas.axes.grid(visible=True)

    def plot(self):
        """
        Plots the data received from the Arduino through the serial port.
        Stops when self.running is set to false.
        Emits finished when done reading input.
        """
        arduino = serial.Serial("/dev/ttyACM0", 115200, timeout=None)
        arduino.write("On".encode())
        val = ([], [])
        coord_list = []
        x = 0
        while (self.running):
            number_str = arduino.readline().decode("ascii")
            if (number_str == "\n"):
                break
            coords = tuple(map(float, number_str.strip().split(' ')))
            gs = sqrt(sum(map(lambda x: x**2, coords)))
            coord_list.append(tuple(coords))
            min_index = max(0, len(val[0]) - 16)
            min_x = min_index * 0.5
            if (min_index > 0):
                del coord_list[0]
            val[1].append(gs)
            val[0].append(x)
            x += 0.5
            self.canvas.axes.clear()
            self.canvas.axes.plot(
                val[0][min_index:], [x for x, _, _ in coord_list], 'r',
                linewidth=0.5, label='Force in x-axis')
            self.canvas.axes.plot(
                val[0][min_index:], [y for _, y, _ in coord_list], 'g',
                linewidth=0.5, label='Force in y-axis')
            self.canvas.axes.plot(
                val[0][min_index:], [z for _, _, z in coord_list], 'b',
                linewidth=0.5, label='Force in z-axis')
            self.canvas.axes.plot(
                val[0][min_index:], val[1][min_index:], 'k', linewidth=1,
                label='Combined g-force')
            self.set_style(min_x)
            self.canvas.draw()
            mean_num = sum(val[1]) / len(val[1])
            # Standard deviation calculation
            sd_num = sqrt(
                sum(map(lambda x: (x - mean_num)**2, val[1])) /
                (len(val[1]) - 1)) if len(val[1]) > 1 else 0
            self.mean.emit(mean_num, sd_num)
            if (coords == 4):
                break
        self.finished.emit()


class Lab1(QMainWindow):

    thread = QThread()

    def __init__(self, *args):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("arduino_sensors")
        self.ui.pushButton.clicked.connect(self.plot_grav)

    def print_extra(self, mean, sd):
        """
        Sets the text of the textbrowser to the given mean
        and standard deviation.
        """
        self.ui.textBrowser.setText(
            "mean: " + format(mean, ".2f") +
            "\nstandard dev. : " + format(sd, ".2f"))

    def plot_grav(self):
        """
        Starts a worker thread which receives input from the
        Arduino and plots the gravitational data in the figure.
        If a thread is running it shuts it down instead.
        """
        if self.thread.isRunning():
            self.worker.running = False
            self.thread.quit()
            self.thread.wait()
        else:
            self.worker = plotter(self.ui.MplWidget.canvas)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.plot)
            self.worker.finished.connect(self.thread.quit)
            self.worker.mean.connect(self.print_extra)
            self.thread.start()


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
